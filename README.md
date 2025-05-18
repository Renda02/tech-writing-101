# Getting Started with Streamlit and Git

This beginner-friendly guide walks you through setting up a Streamlit project with Git version control.

## Installation

### 1. Create a project Folder
```bash
mkdir my_streamlit_app
cd my_streamlit_app
```

### 2. Initialize git repository
```bash
git init
```

### 3. Create a virtual Environment
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
Your command prompt displays `(venv)` at the beginning. For example:
```(venv) my-macbook:my_project```

### 5. Create .gitignore file

Now that you can see what's in your virtual environment folder, create a .gitignore files to ensure the virtual environment is excluded from version control.:
```bash
echo "venv/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".DS_Store" >> .gitignore
```

### 6. Install streamlit
```bash
pip install streamlit
```

### 7. Save dependencies
```bash
pip freeze > requirements.txt
```

### 8. Create a file

Create a file named `app.py` either by clicking on the interface or run> ```touch app.py``

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


