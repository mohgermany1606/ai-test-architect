from src.agents.result_analyzer_agent import (
    result_analyzer_agent
)


def test_result_analyzer_agent():


    state = {

        "requirement": "Search Wikipedia",

        "plan": [],

        "test_cases": [],

        "execution_status": "PASSED",

        "execution_result": "",

        "screenshots": []

    }


    result = result_analyzer_agent(state)


    assert (
        "successful"
        in result["execution_result"]
    )