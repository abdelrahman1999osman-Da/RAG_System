from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ==========================
    # Ollama
    # ==========================
    OLLAMA_HOST: str
    OLLAMA_MODEL: str

 # ==========================
    # openrouter
    # ==========================
    LLM_PROVIDER: str
    OPENROUTER_API_KEY: str
    OPENROUTER_MODEL: str
    
    # ==========================
    # Embedding
    # ==========================
    EMBEDDING_MODEL: str

    # ==========================
    # Book
    # ==========================
    BOOK_NAME: str

    # ==========================
    # Files
    # ==========================
    PDF_PATH: str
    VECTOR_DB_PATH: str

    # Context Builder
    CONTEXT_WORD_BUDGET: int
    SIMILARITY_THRESHOLD: float

    # ==========================
    # Chunking
    # ==========================
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    # ==========================
    # Retrieval
    # ==========================
    TOP_K: int
    FINAL_TOP_K: int

    # Context Builder
    CONTEXT_WORD_BUDGET: int
    SIMILARITY_THRESHOLD: float

    # ==========================
    # LLM
    # ==========================
    TEMPERATURE: float
    MAX_TOKENS: int

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()