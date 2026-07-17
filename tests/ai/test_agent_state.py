from src.agents.state import AgentState


def test_agent_state():

    state: AgentState = {

        "requirement": "Search Wikipedia",

        "test_cases": [],

        "execution_result": "",

        "screenshots": []

    }


    assert state["requirement"] == "Search Wikipedia"

    assert len(state["test_cases"]) == 0