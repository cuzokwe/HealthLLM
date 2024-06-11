from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA
from pinecone import Pinecone, ServerlessSpec
import streamlit as st
from vectorstore import upsert_documents as ud

from docs import load_documents
import os


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

# openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
#
# def generate_response(input_text):
#     llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#     st.info(llm(input_text))
#
# with st.form('my_form'):
#     text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
#     submitted = st.form_submit_button('Submit')
#     if not openai_api_key.startswith('sk-'):
#         st.warning('Please enter your OpenAI API key!', icon='⚠')
#     if submitted and openai_api_key.startswith('sk-'):
#         generate_response(text)


