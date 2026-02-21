import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
from memory_utils import store_memory, retrieve_memories
from llm_utils import extract_memory, generate_response

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("AI Memory Chatbot 🧠")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if st.button("Send") and user_input:

    extracted = extract_memory(client, user_input)
    for mem in extracted:
        store_memory(client, mem)

    retrieved = retrieve_memories(client, user_input)
    response = generate_response(client, user_input, retrieved)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", response))

for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**AI:** {message}")
