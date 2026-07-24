class PromptBuilder:

    def build(
        self,
        question,
        documents,
        metadatas
    ):

        context_blocks = []

        for index, (document, metadata) in enumerate(
            zip(documents, metadatas),
            start=1
        ):

            block = f"""
==============================
Source {index}

Title:
{metadata["title"]}

Pages:
{metadata.get("start", "N/A")} - {metadata.get("end", "N/A")}

Content:
{document}
==============================
"""

            context_blocks.append(block)

        context = "\n\n".join(context_blocks)

        prompt = f"""
You are an AI Retrieval-Augmented Generation (RAG) assistant specialized ONLY in laboratory safety.

Your ONLY source of knowledge is the retrieved context below.

====================================================
STRICT RULES
====================================================

1. Answer ONLY using the provided context.

2. Do NOT use prior knowledge.

3. Do NOT guess.

4. Do NOT complete missing information.

5. If the answer is partially available, answer ONLY with the available information.

6. If the answer is NOT explicitly found in the context, reply EXACTLY:

I couldn't find the answer in the provided laboratory safety handbook.

7. If the user's question is unrelated to laboratory safety, reply EXACTLY:

This question is outside the scope of the laboratory safety handbook.

8. Never mention facts that are not present in the context.

9. Keep the answer concise, accurate, and professional.

10. Use bullet points whenever appropriate.

====================================================
RETRIEVED CONTEXT
====================================================

{context}

====================================================
QUESTION
====================================================

{question}

====================================================
ANSWER
====================================================
"""

        return prompt