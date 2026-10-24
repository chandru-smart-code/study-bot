import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

st.title("🤖 CHANDRU AI Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("")

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are CHANDRU, a smart student AI assistant. Be helpful and friendly."),
    ("user", "{query}")
])

llm = Ollama(model="llama2")
parser = StrOutputParser()
chain = prompt | llm | parser

# Handle input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    response = chain.invoke({"query": user_input})

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

