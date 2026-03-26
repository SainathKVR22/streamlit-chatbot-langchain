from dotenv import load_dotenv
import os
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(
    page_title="Chatbot",
    page_icon="",
    layout="centered",
)

st.title("Generative AI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0,
)

user_input = st.chat_input("Ask chatbot...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role" : "user", "content" : user_input})

    response = llm.invoke(
        input=[{"role" : "system", "content" : "You are an AI helpful assistant, your name is Sai, you have to provide the answer to be concise and accurate"}, *st.session_state.chat_history]

    )

    assistant_response = response.content
    st.session_state.chat_history.append({"role" : "assistant", "content" : assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)