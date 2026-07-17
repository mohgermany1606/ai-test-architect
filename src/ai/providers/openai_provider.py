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


    def ask(self, prompt):

        if self.client is None:
            return """
            [
              {
                "test_id": "TC001",
                "title": "Mock Test Case",
                "steps": [
                    "Open Wikipedia",
                    "Search AI"
                ],
                "expected_result": "Article displayed"
              }
            ]
            """


        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        return response.output_text