# LLM - PERONALIZED SUGGESTIONS

import streamlit as st

# Simple session state Initialization logic
if 'user' in st.session_state:
    pass
else:
    st.session_state.user = None

user = st.selectbox(
    label="Change User",
    options=("User 1", "User 2"),
    index=None) # Initialize selectbox to none

if user is not None:
    st.session_state.user = user

st.write("You are currently:", st.session_state.user)

if st.session_state.user is not None:
    if st.session_state.user == 'User 1':
        st.success('User 1 Profile Selected')
        st.session_state.user = 'user1'
        # switch index namespace

        pass
    if st.session_state.user == 'User 2':
        st.success('User 2 Profile Selected')
        st.session_state.user = 'user2'
        # switch index namespace
        pass

    # Based on the selected user, we can create two different engines/models to feed data to
