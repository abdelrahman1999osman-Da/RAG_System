import streamlit as st

from app.sidebar import sidebar
from app.chat import display_chat

from rag.pipeline import RAGPipeline

st.set_page_config(
    page_title="Chemistry RAG",
    layout="wide"
)

sidebar()

display_chat()

rag = RAGPipeline()

question = st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    result = rag.ask(question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )

    with st.chat_message("assistant"):
        st.markdown(result["answer"])
