from src.agents.planner_agent import planner_agent


def test_planner_agent():


    state = {

        "requirement": 
        "Search Wikipedia for AI",

        "plan": [],

        "test_cases": [],

        "execution_result": "",

        "screenshots": []

    }


    result = planner_agent(state)


    assert len(result["plan"]) > 0


    assert (
        "Generate test scenarios"
        in result["plan"]
    )