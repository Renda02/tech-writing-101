# Getting Started with Streamlit and Git

This beginner-friendly tutorial walks you through setting up a Streamlit project with Git version control.

## Installation

### 1. Create a Project Folder
```bash
mkdir my_streamlit_app
cd my_streamlit_app
```

### 2. Initialize Git Repository
```bash
git init
```

### 3. Create a Virtual Environment
```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment
On macOS/Linux:
```bash
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```
Your command prompt should now show `(venv)` at the beginning.

### 5. Create .gitignore File
Now that you can see what's in your virtual environment folder, exclude it from version control:
```bash
echo "venv/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".DS_Store" >> .gitignore
```

### 6. Install Streamlit
```bash
pip install streamlit
```

### 7. Save Dependencies
```bash
pip freeze > requirements.txt
```

### 8. Create Your First App
Create a file named `app.py` with:
```python
import streamlit as st

st.title('My First Streamlit App')
st.write('Welcome to Streamlit!')
```

### 9. Commit Your Changes
```bash
git add .gitignore requirements.txt app.py
git commit -m "Initial commit: Basic Streamlit setup"
```

### 10. Run Your App
```bash
streamlit run app.py
```

### 11. Push to GitHub (Optional)
```bash
git remote add origin https://github.com/yourusername/my_streamlit_app.git
git branch -M main
git push -u origin main
```

### 12. Deactivate Virtual Environment When Done
```bash
deactivate
```

Build your assistant with [Streamlit cheatsheet](https://docs.streamlit.io/library/cheatsheet)


