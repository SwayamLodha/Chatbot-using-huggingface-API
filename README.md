# 🤖 Hugging Face Conversational Chatbot using Streamlit

This project is a simple **Streamlit-based conversational chatbot** powered by the **Hugging Face Inference API** using the model [`google/gemma-2-2b-it`](https://huggingface.co/google/gemma-2-2b-it).  
It provides a lightweight, interactive web interface that allows users to chat with an AI assistant directly in their browser.

---

## 🧠 Features

- Uses **Hugging Face InferenceClient** for text generation.  
- Maintains **chat history** for contextual replies.  
- Built with **Streamlit** for a clean and interactive UI.  
- Reads your API key securely from a `.env` file.  
- Designed to be **concise and friendly** in responses.

---

## 🗂️ Project Structure

Chat-bot_using_hugging_face/
│
├── app.py # Streamlit front-end app
├── chatbot.py # Core chatbot logic using Hugging Face API
├── .env # Contains your Hugging Face token
└── README.md # Documentation file

##💬 Files Overview
chatbot.py:
This file contains the chatbot logic and the function chat_with_bot() that interacts with the Hugging Face API.

app.py:
This is the Streamlit front-end app that provides the web interface for chatting.

##🧩 Example Usage

- Type your message into the chat box.
- Wait for the AI to respond.
- Enjoy a seamless, interactive conversation.
