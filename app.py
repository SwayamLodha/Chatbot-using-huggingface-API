# app.py
import streamlit as st
from chatbot import chat_with_bot

# Streamlit page configuration
st.set_page_config(page_title="HF Chatbot", page_icon="🤖", layout="centered")

# Title
st.title("🤖 Hugging Face Conversational Chatbot")
st.caption("Created using Hugging Face API and made by Swayam Lodha")

# Session state to maintain chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box for user
user_input = st.chat_input("Type your message...")

# Display chat messages
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# When user submits a message
if user_input:
    # Display user message
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot reply
    bot_reply = chat_with_bot(user_input)

    # Display bot message
    st.session_state.chat_history.append(("assistant", bot_reply))
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
