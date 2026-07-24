import streamlit as st
import os

from config.settings import settings


def sidebar():

    with st.sidebar:

        image_path = "assets/logo.png"

        if os.path.exists(image_path):

            st.image(
                image_path,
                width=220
            )

        else:

            st.warning("Logo not found")

        st.title("Chemistry RAG")

        st.success("Knowledge Base Loaded")

        st.markdown("---")

        st.subheader("📚 Current Book")

        st.write(settings.BOOK_NAME)

        st.markdown("---")

        st.subheader("🤖 Models")

        st.write(f"LLM")
        st.code(settings.OLLAMA_MODEL)

        st.write("Embedding")
        st.code(settings.EMBEDDING_MODEL)

        st.markdown("---")

        st.subheader("⚙️ System Status")

        st.write("✅ Retriever")

        st.write("✅ ChromaDB")

        st.write("✅ Guardrails")

        st.write("✅ LLM Connected")

        st.markdown("---")

        st.info("Running Locally using Ollama + ChromaDB")
