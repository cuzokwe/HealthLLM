import os
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# Initialize the vector store
embeddings = OpenAIEmbeddings()
vectorstore = PineconeVectorStore(index='health-research-index', embedding=embeddings)

# Add document through path spec
loader = TextLoader("../../modules/inaugural_address.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

vectorstore.add_documents(docs)  # add document here

vectorstore.add_texts(['add list of strings here'])  # alternatively, just add string text
