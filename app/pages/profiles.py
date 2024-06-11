# LLM - PERONALIZED SUGGESTIONS

import streamlit as st

user = st.selectbox(
    "Change User",
    ("User 1", "User 2"))

st.write("You are currently:", st.session_state.user)

if user is not None:
    if user == 'User 1':
        st.success('User 1 Profile Selected')
        st.session_state.user = 'user1'
        # switch index namespace

        pass
    if user == 'User 2':
        st.success('User 2 Profile Selected')
        st.session_state.user = 'user2'
        # switch index namespace
        pass

    # Based on the selected user, we can create two different engines/models to feed data to
