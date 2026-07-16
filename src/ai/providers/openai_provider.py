import os

from dotenv import load_dotenv
from openai import OpenAI

from src.ai.providers.base_provider import BaseLLMProvider


load_dotenv()


class OpenAIProvider(BaseLLMProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )


    def generate(self, prompt):

        response = self.client.responses.create(
            model="gpt-4.1",
            input=prompt
        )

        return response.output_text