import json
import re

from src.ai.llm_client import LLMClient
from src.ai.prompts.test_generation import (
    GENERATE_TEST_CASES_PROMPT
)

from src.ai.schemas.test_case import TestCase
from src.utils.ai_logger import ai_logger


class TestGenerator:

    @staticmethod
    def generate(requirement: str):

        ai_logger.info(
            "Starting test case generation"
        )

        # Create prompt
        prompt = GENERATE_TEST_CASES_PROMPT.format(
            requirement=requirement
        )

        ai_logger.info(
            "Prompt created successfully"
        )


        # Call LLM
        response = LLMClient.ask(prompt)


        ai_logger.info(
            "LLM response received"
        )


        # Extract JSON from response
        match = re.search(
            r"```json\s*(.*?)\s*```",
            response,
            re.DOTALL
        )


        if match:

            json_text = match.group(1)

            ai_logger.info(
                "JSON extracted from markdown block"
            )

        else:

            json_text = response

            ai_logger.info(
                "Response treated as plain JSON"
            )


        # Convert JSON string to Python object
        try:

            data = json.loads(json_text)

            ai_logger.info(
                f"JSON parsing successful. "
                f"Received {len(data)} test cases"
            )


        except Exception as e:

            ai_logger.error(
                f"JSON parsing failed: {e}"
            )

            raise


        # Validate using Pydantic
        try:

            test_cases = [
                TestCase.model_validate(item)
                for item in data
            ]


            ai_logger.info(
                "AI response validation successful"
            )


            return test_cases


        except Exception as e:

            ai_logger.error(
                f"Pydantic validation failed: {e}"
            )

            raise