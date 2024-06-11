# LLM - PERONALIZED SUGGESTIONS

import streamlit as st

user = st.selectbox(
    "Select User Profile",
    ("User 1", "User 2"))

st.write("You selected:", user)

if user is not None:
    if user == 'User 1':
        st.success('User 1 Profile Selected')
        pass
    if user == 'User 2':
        st.success('User 2 Profile Selected')
        pass

    # Based on the selected user, we can create two different engines/models to feed data to
