# Tech Writing Assistant: A Streamlit style guide application 

This beginner-friendly tutorial walks you through setting up a tech writing assistant app with Streamlit and Git version control.

## Overview

The Tech Writing Assistant is a web application built with Streamlit that helps writers adhere to technical writing best practices. It leverages OpenAI's GPT-4 model to analyze text input and provide style suggestions based on a comprehensive style guide. The app identifies issues with passive voice, nominalization, sentence length, formatting, and more, then offers specific improvements with explanations.

## What we cover

In this guide, you'll learn:

- Setting up a development environment with virtual environments and Git
- Installing Streamlit and OpenAI Python packages
- Building a user interface with Streamlit components
- Integrating OpenAI's API for text analysis
- Implementing error handling for API interactions

## Prerequisites

Before you begin, make sure you have:

- Python 3.7 or higher installed
- Basic knowledge of Python programming
- Git installed on your system
- An OpenAI API key (sign up at https://platform.openai.com)
- Basic understanding of terminal/command line operations
- Text editor or IDE of your choice (VS Code recommended)
- Internet connection for package installation and API calls

## Installation

### 1. Create a project folder
```bash
mkdir project-folder-name
cd project-folder-name
```
Replace `project-folder-name` with a meaningful name.

### 2. Initialize Git repository
```bash
git init
```

### 3. Create a virtual environment
```bash
python3 -m venv venv
```

### 4. Activate the virtual environment
On macOS/Linux:
```bash
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```
Your command prompt should now show `(venv)` at the beginning.

### 5. Create .gitignore file
```bash
echo "venv/" >> .gitignore
```

### 6. Install required packages
```bash
pip install streamlit openai
```

### 7. Deactivate virtual environment when done
```bash
deactivate
```

## Building the tech writing assistant app

The Tech Writing assistant app:

- Enforces a comprehensive style guide for technical writing
- Provides specific feedback on style, grammar, tone, and formatting
- Suggests improvements to align with the style guide
- Allows users to download suggestions as a markdown file

## Style guide highlights

The app enforces these style principles:
- Active voice, not passive
- Present tense writing
- Concise language without unnecessary words
- Maximum sentence length of 26 words
- Proper formatting for lists
- Positive language
- Proper acronym usage
- Oxford commas
- Numbered lists for sequential processes
- Bulleted lists for non-sequential items

### 1. Create the basic app structure
Create a file named `app.py` with the basic Streamlit structure:

```python
import streamlit as st

st.title('Tech writing assistant')
st.write('Welcome to your tech writing assistant!')
```

### 2. Run your app
```bash
streamlit run app.py
```

### 3. Add OpenAI integration
Update your app.py to include OpenAI integration:

```python
import streamlit as st
from openai import OpenAI

# Sidebar: API key input
st.sidebar.title("Settings")
api_key_input = st.sidebar.text_input(
    "Enter your OpenAI API Key",
    type="password",
    help="Get your API key at https://platform.openai.com/account/api-keys"
)

if api_key_input:
    client = OpenAI(api_key=api_key_input)
else:
    client = None

# Main app title
st.title("Tech writing assistant")

# Warn if no API key provided
if not client:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()
```

### 4. Add text input and analysis functionality
Expand your app to include text input and analysis:

```python
# User text input
st.write("Enter your text below for style analysis.")
user_input = st.text_area("Your text", height=300)

if st.button("Analyze text"):
    if not user_input.strip():
        st.warning("Enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            # Add analysis code here
            st.success("Analysis complete!")
```

### 5. Implement the complete tech writing assistant
The complete app includes:
- API key management
- Text input area
- Style guide enforcement
- Error handling
- Downloadable suggestions

The full implementation is in the app.py file.

### 6. Commit your changes
```bash
git add .gitignore requirements.txt app.py
git commit -m "Initial commit: Tech writing assistant app"
```

### 7. Push to GitHub (optional)
```bash
git remote add origin https://github.com/yourusername/tech_writing_assistant.git
git branch -M main
git push -u origin main
```

### 8. Manage your virtual environment

Once you're finished working on your project, you can deactivate the virtual environment:

```bash
deactivate
```

## Troubleshooting

If you encounter OpenAI API errors, the app provides clear feedback for:
- Authentication errors
- Rate limit issues
- Connection problems

## Resources

- See [Streamlit cheatsheet](https://docs.streamlit.io/library/cheatsheet) for Streamlit commands and code examples for creating various UI elements, displaying data, and managing the app state.
