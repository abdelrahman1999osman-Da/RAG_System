from openai import OpenAI

from config.settings import settings


class OpenRouterLLM:

    def __init__(self):

        self.client = OpenAI(

            api_key=settings.OPENROUTER_API_KEY,

            base_url="https://openrouter.ai/api/v1"

        )

        self.model = settings.OPENROUTER_MODEL

    def generate(self, prompt: str):

        response = self.client.chat.completions.create(

            model=self.model,

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=settings.TEMPERATURE,

            max_tokens=settings.MAX_TOKENS

        )

        return response.choices[0].message.content