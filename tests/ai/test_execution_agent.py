from unittest.mock import patch
from src.ai.schemas.test_case import TestCase
from src.agents.execution_agent import execution_agent


def test_execution_agent():

    state = {

    "test_cases": [

        TestCase(
            test_id="TC001",
            title="Open Wikipedia",
            steps=[
                "Open Wikipedia"
            ],
            expected_result="Wikipedia opens"
        )

    ],

    "execution_status": "",

    "execution_result": "",

    "screenshots": []

}


    with patch(
        "src.agents.execution_agent.execute_action"
    ) as mock_execute:


        result = execution_agent(
            state
        )


    assert result["execution_status"] == "PASSED"

    assert (
        result["execution_result"]
        ==
        "Test executed successfully"
    )

    assert len(result["screenshots"]) == 1