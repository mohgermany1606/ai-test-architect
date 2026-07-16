from unittest.mock import patch

from src.ai.test_generator import TestGenerator


MOCK_RESPONSE = """
[
    {
        "test_id": "TC001",
        "title": "Search Wikipedia",
        "steps": [
            "Open Wikipedia",
            "Search Artificial Intelligence"
        ],
        "expected_result": "Article is displayed"
    }
]
"""


def test_generate_test_cases():

    with patch(
        "src.ai.llm_client.LLMClient.ask"
    ) as mock_llm:

        mock_llm.return_value = MOCK_RESPONSE

        tests = TestGenerator.generate(
            "User searches Wikipedia for AI"
        )

        assert len(tests) == 1
        assert tests[0].test_id == "TC001"
        assert tests[0].title == "Search Wikipedia"
        assert len(tests[0].steps) == 2



def test_invalid_ai_response():

    INVALID_RESPONSE = """
    [
        {
            "test_id": "TC001"
        }
    ]
    """

    with patch(
        "src.ai.llm_client.LLMClient.ask"
    ) as mock_llm:

        mock_llm.return_value = INVALID_RESPONSE

        try:

            TestGenerator.generate(
                "Invalid AI response test"
            )

            assert False

        except Exception:

            assert True