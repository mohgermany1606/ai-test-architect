from src.ai.providers.openai_provider import OpenAIProvider
from src.utils.ai_logger import ai_logger


class LLMClient:

    provider = OpenAIProvider()


    @staticmethod
    def ask(prompt):

        ai_logger.info(
            "Sending prompt to LLM"
        )

        ai_logger.info(
            prompt
        )


        response = LLMClient.provider.generate(
            prompt
        )


        ai_logger.info(
            "LLM response received"
        )

        ai_logger.info(
            response
        )


        return response