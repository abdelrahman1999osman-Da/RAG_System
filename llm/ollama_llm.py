from ollama import Client

from config.settings import settings


class OllamaLLM:

    def __init__(self):

        self.client = Client(
            host=settings.OLLAMA_HOST
        )

        self.model = settings.OLLAMA_MODEL

    def generate(self, prompt: str):

        response = self.client.generate(

            model=self.model,

            prompt=prompt,

            options={
                "temperature": settings.TEMPERATURE,
                "num_predict": settings.MAX_TOKENS
            }

        )

        print("=" * 80)
        print("OLLAMA RESPONSE")
        print(response)
        print("=" * 80)

        return response["response"]