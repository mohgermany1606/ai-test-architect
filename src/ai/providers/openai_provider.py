import os
from openai import OpenAI


class OpenAIProvider:


    def __init__(self):

        api_key = os.getenv(
            "OPENAI_API_KEY"
        )

        if api_key == "test-key":
            self.client = None
            return


        self.client = OpenAI(
            api_key=api_key
        )