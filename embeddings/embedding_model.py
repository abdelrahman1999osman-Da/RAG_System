from sentence_transformers import SentenceTransformer
from config.settings import settings


class EmbeddingModel:

    def __init__(self):

        print(f"Loading embedding model: {settings.EMBEDDING_MODEL}")

        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

        self.dimension = self.model.get_sentence_embedding_dimension()

        print(f"Embedding dimension: {self.dimension}")

    def get_dimension(self):

        return self.dimension

    def embed(self, text: str):

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()