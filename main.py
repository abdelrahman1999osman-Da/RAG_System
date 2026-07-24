import shutil
import os

from config.settings import settings

from loaders.pdf_loader import PDFLoader
from preprocessing.text_cleaner import TextCleaner
from preprocessing.chunker import Chunker
from embeddings.embedding_model import EmbeddingModel
from vectorstore.chroma_manager import ChromaManager
from retrievers.retriever import Retriever


# ==========================================================
# Settings
# ==========================================================

print(f"Ollama Host : {settings.OLLAMA_HOST}")
print(f"LLM Model   : {settings.OLLAMA_MODEL}")
print(f"Embedding   : {settings.EMBEDDING_MODEL}")
print(f"Chunk Size  : {settings.CHUNK_SIZE}")
print(f"Vector DB   : {settings.VECTOR_DB_PATH}")


# ==========================================================
# 0. Reset Vector Database
# ==========================================================

if os.path.exists(settings.VECTOR_DB_PATH):

    shutil.rmtree(settings.VECTOR_DB_PATH)

    print(f"Deleted old vector database at: {settings.VECTOR_DB_PATH}")

else:

    print("No existing vector database found. Starting fresh.")


# ==========================================================
# 1. Load PDF
# ==========================================================

loader = PDFLoader()
documents = loader.load()

print("=" * 80)
print("FIRST DOCUMENT")
print("=" * 80)
print(documents[0]["title"])
print(documents[0]["text"][:3000])
print("=" * 80)


# ==========================================================
# 2. Clean Text
# ==========================================================

cleaner = TextCleaner()

for document in documents:
    document["text"] = cleaner.clean(document["text"])


# ==========================================================
# 3. Create Chunks
# ==========================================================

chunker = Chunker()
chunks = chunker.create_chunks(documents)

print(f"Documents : {len(documents)}")
print(f"Chunks    : {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])


# ==========================================================
# 4. Test Embedding
# ==========================================================

embedding_model = EmbeddingModel()

embedding = embedding_model.embed(
    chunks[0]["chunk_text"]
)

print(f"\nEmbedding Size: {len(embedding)}")
print(embedding[:10])


# ==========================================================
# 5. Build Vector Database
# ==========================================================

vector_db = ChromaManager()

print("Current vectors:", vector_db.collection.count())

vector_db.add_documents(
    chunks,
    embedding_model
)

print("Current vectors:", vector_db.collection.count())
print("Vector Database Created Successfully")


# ==========================================================
# 6. Test Retrieval
# ==========================================================

retriever = Retriever()

results = retriever.search(
    "What should I do if sulfuric acid spills?"
)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(results["documents"][0]):

    print(f"\n---------- Result {i+1} ----------")
    print(doc[:500])

print("\nMetadata:\n")

for meta in results["metadatas"][0]:

    print(meta)
