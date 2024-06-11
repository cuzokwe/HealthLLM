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

# create vectorstore in Pinecone and load it with OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
documents = load_documents(["./research"])  # dataloader
vectorstore = PineconeVectorStore.from_documents(documents, index_name='health-research-index', embedding=embeddings)

# start LLM attached to OpenAI backend
llm = OpenAI()
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# query
query = "Who is the 47th president?"
result = qa_chain.run(query)

print(result)