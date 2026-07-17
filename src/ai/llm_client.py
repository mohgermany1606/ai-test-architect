from src.ai.providers.openai_provider import OpenAIProvider


class LLMClient:

    provider = None


    @staticmethod
    def ask(prompt):

        if LLMClient.provider is None:
            LLMClient.provider = OpenAIProvider()

        return LLMClient.provider.ask(prompt)