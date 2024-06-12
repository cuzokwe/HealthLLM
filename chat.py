import os
import random

import streamlit as st
from langchain.llms import OpenAI

class CurieChat:
    def __init__(self):
        self.api_key = os.environ["OPEN_AI_KEY"]

        if "messages" not in st.session_state:
            st.session_state["messages"] = []

        self.messages = st.session_state["messages"]

        self.create_chat()

    def create_chat(self):
        user_input = st.chat_input("Ask Curie")

        with st.form("Curie"):
            self.load_old_messages()
            if user_input:
                with st.chat_message("User", avatar="./images/person.png"):
                    st.write(user_input)
                    self.messages.append({"user": user_input})

                response = self.generate_response(user_input)
                with st.chat_message("Curie", avatar="./images/curie.png"):
                    st.write(response)
                    self.messages.append({"curie": response})

            st.markdown("""
                        <style>
                        [data-testid="stFormSubmitButton"] {display: none;}
                        </style>
                    """, unsafe_allow_html=True)
            button = st.form_submit_button("")


    def load_old_messages(self):
        for message in self.messages:
            name, value = list(message.items())[0]

            if name == "user":
                user = st.chat_message("User", avatar="./images/person.png")
                user.write(value)

            elif name == "curie":
                curie = st.chat_message("Curie", avatar="./images/curie.png")
                curie.write(value)


    def generate_response(self, text):
        # llm = OpenAI(temperature=0.7, openai_api_key=self.api_key)
        # result = llm(text)

        result = random.random()

        return result