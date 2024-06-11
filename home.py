import streamlit as st
from langchain.llms import OpenAI
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA
from pinecone import Pinecone, ServerlessSpec

from docs import load_documents
import os

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    embeddings = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore(index_name='health-research-index', embedding=embeddings)
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())
    st.info(qa_chain.run(input_text))



with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
