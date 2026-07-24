class Reranker:

    def rerank(self, results, top_n=3):

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        rows = []

        for doc, meta, distance in zip(
            documents,
            metadatas,
            distances
        ):

            rows.append({

                "document": doc,

                "metadata": meta,

                "distance": distance

            })

        # كلما كانت الـ distance أصغر كان التشابه أعلى
        rows.sort(key=lambda x: x["distance"])

        return rows[:top_n]