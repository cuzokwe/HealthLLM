import streamlit as st
from vectorstore import upsert_documents as ud

import os

## LLM Learning Information via PDF Upload
def save_uploaded_file(uploaded_file):
    # Define the path where the file will be saved
    save_path = f"./research/{uploaded_file.name}"

    # Save the file to the specified path
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return save_path

uploaded_file = st.file_uploader('Health Document Upload', type="pdf")
if uploaded_file is not None:
    cwd = os.getcwd()
    # Save the uploaded file to the file system
    file_path = save_uploaded_file(uploaded_file)

    st.success(f"File saved to {file_path}")
    full_file_path = cwd + file_path[1:]
    print(full_file_path)
    ud.upload_file_to_vectorstore(full_file_path)


