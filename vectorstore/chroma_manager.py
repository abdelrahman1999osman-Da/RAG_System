import chromadb

from config.settings import settings


class ChromaManager:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.VECTOR_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name="chemistry_book",
            metadata={"hnsw:space": "cosine"}
        )
        print("VECTOR DB PATH:", settings.VECTOR_DB_PATH)
        print("COLLECTION COUNT:", self.collection.count())


    def add_documents(self, chunks, embedding_model):

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for chunk in chunks:

            ids.append(chunk["chunk_id"])

            documents.append(chunk["chunk_text"])

            embeddings.append(
                embedding_model.embed(chunk["chunk_text"])
            )

            metadatas.append({

                "document_id": str(chunk["document_id"]),

                "title": chunk["title"],

                "page_start": str(chunk["page_start"]),

                "page_end": str(chunk["page_end"])

            })

        self.collection.add(

            ids=ids,

            documents=documents,

            embeddings=embeddings,

            metadatas=metadatas

        )