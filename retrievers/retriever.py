from config.settings import settings

from embeddings.embedding_model import EmbeddingModel
from vectorstore.chroma_manager import ChromaManager


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()
        self.vector_db = ChromaManager()

    def search(self, query: str, top_k: int = None):

        if top_k is None:
            top_k = settings.TOP_K

        query_embedding = self.embedding_model.embed(query)

        results = self.vector_db.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )

        # ==========================
        # Debug
        # ==========================
        print("\n" + "=" * 80)
        print("RETRIEVAL RESULTS")
        print("=" * 80)

        for i, (meta, distance) in enumerate(
            zip(results["metadatas"][0], results["distances"][0]),
            start=1
        ):
            print(
                f"{i:2d}. Distance = {distance:.6f} | {meta['title']}"
            )

        print("=" * 80)

        return results