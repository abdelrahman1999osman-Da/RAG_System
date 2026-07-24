from config.settings import settings


class Chunker:

    def __init__(self):
        self.chunk_size = settings.CHUNK_SIZE
        self.chunk_overlap = settings.CHUNK_OVERLAP

    def split_text(self, text: str):

        words = text.split()

        chunks = []
        start = 0

        while start < len(words):

            end = start + self.chunk_size

            chunks.append(" ".join(words[start:end]))

            if end >= len(words):
                break

            start += self.chunk_size - self.chunk_overlap

        return chunks

    def create_chunks(self, documents):

        chunk_rows = []

        for document in documents:

            chunks = self.split_text(document["text"])

            for index, chunk in enumerate(chunks):

                chunk_rows.append({

                    "chunk_id": f"doc{document['document_id']}_chunk{index}",

                    "document_id": document["document_id"],

                    "title": document["title"],

                    "chunk_index": index,

                    "page_start": document["page_start"],

                    "page_end": document["page_end"],

                    "chunk_text": chunk,

                    "search_text": f"{document['title']} {chunk}"

                })

        return chunk_rows