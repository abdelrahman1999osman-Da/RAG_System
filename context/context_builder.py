from config.settings import settings


class ContextBuilder:

    def build(
        self,
        documents,
        metadatas,
        distances=None,
        max_chunks=None,
        word_budget=None,
    ):

        if max_chunks is None:
            max_chunks = settings.FINAL_TOP_K

        if word_budget is None:
            word_budget = settings.CONTEXT_WORD_BUDGET

        selected_documents = []
        selected_metadatas = []

        total_words = 0

        chapter_counter = {}

        for document, metadata in zip(documents, metadatas):

            title = metadata.get("title", "")

            # -----------------------------------
            # Ignore Table of Contents
            # -----------------------------------

            if "Table of Contents" in title:
                continue

            # -----------------------------------
            # Maximum 2 chunks from each chapter
            # -----------------------------------

            if chapter_counter.get(title, 0) >= 2:
                continue

            words = len(document.split())
            print("CHUNK WORDS:", words)
            print("WORD BUDGET:", word_budget)

            if total_words + words > word_budget:
                print(f"SKIPPED CHUNK: {words} words > remaining budget")
                continue

            selected_documents.append(document)
            selected_metadatas.append(metadata)

            total_words += words

            chapter_counter[title] = chapter_counter.get(title, 0) + 1

            if len(selected_documents) >= max_chunks:
                break

        print("\n" + "=" * 80)
        print("FINAL CONTEXT")
        print("=" * 80)

        for i, meta in enumerate(selected_metadatas, start=1):

            print(
                f"{i}. {meta['title']} "
                f"(Pages {meta['page_start']} - {meta['page_end']})"
            )

        print("=" * 80)

        return selected_documents, selected_metadatas