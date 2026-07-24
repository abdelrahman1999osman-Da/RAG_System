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

        # ==========================================================
        # DEBUG
        # ==========================================================
        print("\n" + "=" * 80)
        print("QUERY:")
        print(query)
        print("=" * 80)

        print(f"Retrieved Documents : {len(results['documents'][0])}")
        print(f"Retrieved Metadata  : {len(results['metadatas'][0])}")
        print(f"Retrieved Distances : {len(results['distances'][0])}")

        print("=" * 80)
        print(f"{'#':<4} {'Distance':<12} {'Title'}")
        print("=" * 80)

        for i, (doc, meta, distance) in enumerate(
            zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            ),
            start=1
        ):

            print(
                f"{i:<4} {distance:<12.6f} {meta.get('title', 'Unknown')}"
            )

            print("Chunk Preview:")
            print(doc[:200].replace("\n", " "))
            print("-" * 80)

        return results