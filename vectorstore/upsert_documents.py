import os
from typing import List
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
import streamlit as st

def upload_file_to_vectorstore(file_path: str, pinecone_index: str = 'health-research-index', chunk_size: int = 1000, chunk_overlap: int = 0):
    """
    Uploads a file to the Pinecone vector store.

    Args:
        file_path (str): The path to the file to be uploaded.
        pinecone_index (str): The name of the Pinecone index to use.
        chunk_size (int, optional): The maximum size of text chunks. Defaults to 1000.
        chunk_overlap (int, optional): The overlap between text chunks. Defaults to 0.

    Returns:
        None
    """

    pc = Pinecone(api_key=os.environ['PINECONE_API_KEY'])
    index = pc.Index(pinecone_index)

    # Initialize the vector store and embeddings
    embeddings = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore(index=index, namespace=st.session_state.user, embedding=embeddings)

    # Determine the file type and load the file
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == ".pdf":
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)
    documents = loader.load()

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)

    # Upload the chunks to the vector store
    vectorstore.add_documents(docs)

# Example usage
# upload_file_to_vectorstore("path/to/file.pdf", "health-research-index")
# upload_file_to_vectorstore("path/to/text_file.txt", "health-research-index", chunk_size=500, chunk_overlap=50)