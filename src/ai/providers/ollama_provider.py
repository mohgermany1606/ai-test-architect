from langchain_ollama import ChatOllama

from src.ai.providers.base_provider import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):

    def __init__(self):

        self.model = ChatOllama(
            model="llama3.1"
        )


    def generate(self, prompt):

        response = self.model.invoke(
            prompt
        )

        return response.content