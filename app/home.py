import streamlit as st
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
import os



def generate_response(input_text):
    embeddings = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore(index_name='health-research-index', embedding=embeddings)
    llm = ChatOpenAI(openai_api_key=os.environ['OPENAI_API_KEY'], temperature=0.0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())
    print(input_text)
    st.info(qa_chain.run(input_text))


def main():
    st.title('🦜🔗 Quickstart App')

    with st.form('my_form'):
        text = st.text_area('Enter text:', 'What are some ways I can increase my metabolism?')
        submitted = st.form_submit_button('Submit')
        if submitted:
            generate_response(text)


if __name__ == '__main__':
    main()
