import streamlit as st

from app.sidebar import sidebar
from app.chat import display_chat
from rag.pipeline import RAGPipeline
from config.settings import settings
from build_index import build_index
from vectorstore.chroma_manager import ChromaManager


st.set_page_config(
    page_title="Chemical Laboratory Safety Assistant",
    page_icon="🧪",
    layout="wide"
)

def load_css():

    with open("app/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

# ==========================================================
# Build Vector DB automatically (first run only)
# ==========================================================

vector_db = ChromaManager()

if vector_db.collection.count() == 0:

    with st.spinner("Building vector database... This may take a minute."):

        build_index()

    st.success("Vector database created successfully.")

st.title("🧪 RAG System v999")

st.markdown(f"""
### AI-Powered Retrieval-Augmented Generation (RAG)

This assistant answers questions based on the **{settings.BOOK_NAME}** handbook using a local AI model.

---
""")

st.subheader("💡 Example Questions")

col1, col2 = st.columns(2)

with col1:
    st.markdown("- What PPE should I wear?")
    st.markdown("- What should I do after an acid spill?")
    st.markdown("- How should chemical waste be disposed?")

with col2:
    st.markdown("- Fire emergency procedures")
    st.markdown("- How should chemicals be stored?")
    st.markdown("- What are the laboratory safety rules?")

st.divider()


sidebar()

display_chat()

rag = RAGPipeline()


question = st.chat_input(
    "Ask about laboratory safety..."
)


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
    print(result)

    answer = result["answer"]

    sources = result["sources"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):

        st.markdown(answer)

        if sources:

            st.divider()

            st.caption("📚 Sources")

            shown = set()

            for source in sources:

                key = (
                    source["title"],
                    source["page_start"],
                    source["page_end"]
                )

                if key not in shown:

                    shown.add(key)

                    st.write(
                        f"📖 **{source['title']}** "
                        f"(Pages {source['page_start']} - {source['page_end']})"
                    )