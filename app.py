import streamlit as st
from openai import OpenAI
from openai._exceptions import (
    APIError,
    APIConnectionError,
    AuthenticationError,
    RateLimitError,
)
import io

# Style guide
STYLE_GUIDE = """
Write in active voice, not passive. 
Prefer verbs over nouns (avoid nominalizations).
Write in the present tense; avoid using "will".
Cut unnecessary words and prefer shorter constructions (e.g., use "can" instead of "will be able to").
Avoid clipped language, such as omitting articles like "the".
Limit sentences to a maximum of 26 words.
Use descriptive link text.
Put conditional clauses before instructions.
Format lists correctly; ensure lists are grammatically and conceptually parallel. This is very important.
Use positive language, not negative language. Avoid double negatives (i.e., never use double negatives).
Do not preannounce anything.
Use sentence case for titles and headings where only the first word and proper nouns are capitalized.
Use "allow" only to refer to permissions; otherwise, use "let".
Define acronyms when first used. Do not use acronyms in headings. Do not introduce acronyms if the term appears only a few times.
Put full stops after links at the end of a sentence, but not after email addresses.
Put full stops at the end of complete sentences, but not incomplete ones.
Avoid corporate jargon such as "reach out". Prefer standard words like "contact" or "email".
Do not say "please".
Use Oxford/serial commas.
Do not use ampersands (&).
Write all numbers as numerals, including 1 through 10.
Use numbered lists for processes where order matters.
Use bulleted lists for non-processes where order does not matter.
"""

# Sidebar: API key input
st.sidebar.title("Settings")
api_key_input = st.sidebar.text_input(
    "Enter your OpenAI API Key",
    type="password",
    value=st.session_state.get("OPENAI_API_KEY", ""),
    help="Get your API key at https://platform.openai.com/account/api-keys"
)

if api_key_input:
    st.session_state["OPENAI_API_KEY"] = api_key_input
    client = OpenAI(api_key=api_key_input)
else:
    client = None

# Main app
st.title("Tech writing assistant")

if not client:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()

st.write("Enter your text below. The assistant will provide suggestions to align it with the style guide.")

user_input = st.text_area("Your text", height=300)

if st.button("Check Style"):
    if not user_input.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": f"You are an editorial assistant. Enforce this style guide:\n{STYLE_GUIDE}"},
                        {"role": "user", "content": f"Analyze this text and provide style suggestions:\n\n{user_input}"}
                    ],
                    temperature=0.3,
                    max_tokens=800,
                )
                suggestions = response.choices[0].message.content
                st.subheader("Suggestions:")
                st.markdown(suggestions)

                # Download as markdown
                md_file = io.StringIO(suggestions)
                st.download_button(
                    label="📥 Download Suggestions as Markdown",
                    data=md_file.getvalue(),
                    file_name="style_suggestions.md",
                    mime="text/markdown"
                )

            except AuthenticationError:
                st.error("Invalid API key. Please check and try again.")
            except RateLimitError:
                st.error("Rate limit exceeded. Please wait and try again later.")
            except APIConnectionError:
                st.error("Failed to connect to OpenAI servers. Check your internet connection.")
            except APIError as e:
                st.error(f"Unexpected OpenAI error: {str(e)}")
