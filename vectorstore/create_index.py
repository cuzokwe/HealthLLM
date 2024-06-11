from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA
from pinecone import Pinecone, ServerlessSpec

from docs import load_documents
import os

# start pinecone & create index
pc = Pinecone(api_key=os.environ['PINECONE_API_KEY'])

try:
    pc.create_index(
        name="health-research-index",
        dimension=1536,  # Replace with your model dimensions
        metric="euclidean",  # Replace with your model metric
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

except:
    pass