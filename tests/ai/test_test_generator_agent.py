from unittest.mock import patch

from src.agents.test_generation_agent import generate_tests_agent


def test_test_generator_agent():


    state = {

        "requirement": 
        "Search Wikipedia for AI",

        "plan": [],

        "test_cases": [],

        "execution_result": "",

        "screenshots": []

    }


    with patch(
        "src.agents.test_generation_agent.TestGenerator.generate"
    ) as mock_generate:


        mock_generate.return_value = [

            {
                "test_id": "TC001",

                "title": "Search AI",

                "steps": [
                    "Open Wikipedia"
                ],

                "expected_result":
                "Article displayed"

            }

        ]


        result = generate_tests_agent(
            state
        )


        assert len(
            result["test_cases"]
        ) == 1