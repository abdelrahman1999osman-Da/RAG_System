# RAG Laboratory Safety Assistant

An intelligent Retrieval-Augmented Generation (RAG) system that answers laboratory safety questions using the **Prudent Practices in the Laboratory** handbook.

The system retrieves the most relevant information from the handbook, builds an optimized context, and generates accurate responses using either **Ollama** or **OpenRouter** Large Language Models.

---

## Features

- PDF document processing
- Text cleaning and chunking
- Semantic embeddings
- ChromaDB vector database
- Semantic retrieval
- Context Builder
- Semantic Guardrails
- Prompt Engineering
- Multiple LLM providers
  - Ollama
  - OpenRouter
- Streamlit Web Interface
- Retrieval Evaluation
  - Precision@K
  - Recall@K
  - Hit Rate
  - MRR

---

## System Architecture

```
User Question
      │
      ▼
Semantic Guardrails
      │
      ▼
Retriever
      │
      ▼
Context Builder
      │
      ▼
Prompt Builder
      │
      ▼
LLM
(Ollama / OpenRouter)
      │
      ▼
Answer + Sources
```

---

## Project Structure

```
RAG-System/

├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── config/
├── loaders/
├── preprocessing/
├── embeddings/
├── vectorstore/
├── retrievers/
├── context/
├── guardrails/
├── prompts/
├── llm/
├── rag/
│
├── data/
├── chroma_db/
└── assets/
```

---

## Technologies

- Python
- ChromaDB
- Sentence Transformers
- Ollama
- OpenRouter
- Streamlit
- PyMuPDF
- Pydantic
- NumPy

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/RAG-System.git

cd RAG-System
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

Example:

```env
LLM_PROVIDER=ollama

OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen3:8b

OPENROUTER_API_KEY=

OPENROUTER_MODEL=openai/gpt-4.1-mini

CHUNK_SIZE=500
CHUNK_OVERLAP=100

TOP_K=5
FINAL_TOP_K=3

SIMILARITY_THRESHOLD=0.60
GUARDRAILS_THRESHOLD=0.47

TEMPERATURE=0.2
MAX_TOKENS=512
```

---

## Running the Application

```bash
streamlit run app.py
```

---

## Example Questions

- What PPE should I wear when working with chemicals?
- What should I do if sulfuric acid spills?
- How should chemical waste be disposed of?
- What are the recommended laboratory techniques?

---

## Evaluation

The retriever was evaluated using:

- Precision@K
- Recall@K
- Hit Rate
- Mean Reciprocal Rank (MRR)

---

## Future Improvements

- Cross-Encoder Re-ranking
- Hybrid Retrieval (BM25 + Dense Retrieval)
- Conversation Memory
- Multi-document RAG
- Citation-aware Answer Generation
- Docker Deployment
- CI/CD Pipeline

---

