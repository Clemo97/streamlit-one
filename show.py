# Read the content of an external Python file (e.g., myfile.py)
with open('myfile.py', 'r') as file:
    python_code = file.read()

# Create a Streamlit app
st.title("Display Python Code")

# Display the content of the file in a st.code block
st.code(python_code, language="python")