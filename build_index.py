from loaders.pdf_loader import PDFLoader
from preprocessing.text_cleaner import TextCleaner
from preprocessing.chunker import Chunker
from embeddings.embedding_model import EmbeddingModel
from vectorstore.chroma_manager import ChromaManager


def build_index():

    print("=" * 80)
    print("Building Vector Database...")
    print("=" * 80)

    # 1. Load PDF
    loader = PDFLoader()
    documents = loader.load()

    # 2. Clean Text
    cleaner = TextCleaner()

    for document in documents:
        document["text"] = cleaner.clean(document["text"])

    # 3. Chunking
    chunker = Chunker()
    chunks = chunker.create_chunks(documents)

    print(f"Documents : {len(documents)}")
    print(f"Chunks    : {len(chunks)}")

    # 4. Embeddings
    embedding_model = EmbeddingModel()

    # 5. Vector Store
    vector_db = ChromaManager()

    # لو فيه بيانات قديمة امسحها
    if vector_db.collection.count() > 0:
        vector_db.collection.delete(
            ids=vector_db.collection.get()["ids"]
        )

    vector_db.add_documents(
        chunks,
        embedding_model
    )

    print(f"Vectors : {vector_db.collection.count()}")
    print("Vector Database Built Successfully.")


if __name__ == "__main__":
    build_index()