from retrievers.retriever import Retriever
from prompts.prompt_builder import PromptBuilder
from llm.ollama_llm import OllamaLLM
from llm.openrouter_llm import OpenRouterLLM
from context.context_builder import ContextBuilder
from config.settings import settings


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.context_builder = ContextBuilder()

        # Choose LLM Provider
        if settings.LLM_PROVIDER.lower() == "ollama":

            self.llm = OllamaLLM()

        elif settings.LLM_PROVIDER.lower() == "openrouter":

            self.llm = OpenRouterLLM()

        else:

            raise ValueError(
                f"Unsupported LLM Provider: {settings.LLM_PROVIDER}"
            )

    def ask(self, question: str):

        # -----------------------------
        # 1. Retrieve
        # -----------------------------
        results = self.retriever.search(question)
        

        if (
            "documents" not in results
            or not results["documents"]
            or not results["documents"][0]
        ):
            return {
                "answer": (
                    "I couldn't find relevant information "
                    "in the laboratory safety handbook."
                ),
                "sources": []
            }

        # -----------------------------
        # 2. Build Context
        # -----------------------------
        documents, metadatas = self.context_builder.build(

            documents=results["documents"][0],

            metadatas=results["metadatas"][0],

            distances=results["distances"][0]

          )

        if not documents:

            return {
                "answer": (
                    "I couldn't find enough relevant information "
                    "to answer your question."
                ),
                "sources": []
            }

        # -----------------------------
        # 3. Build Prompt
        # -----------------------------
        prompt = self.prompt_builder.build(

            question=question,

            documents=documents,

            metadatas=metadatas

        )

        # -----------------------------
        # 4. Generate Answer
        # -----------------------------
        answer = self.llm.generate(prompt)

        return {

            "answer": answer,

            "sources": metadatas

        }