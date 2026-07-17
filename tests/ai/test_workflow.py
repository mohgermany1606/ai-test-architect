from src.graph.workflow import create_workflow


def test_workflow_execution():

    app = create_workflow()


    state = {

        "requirement": 
        "Search Wikipedia for AI",

        "plan": [],

        "test_cases": [],

        "execution_status": "",

        "execution_result": "",

        "screenshots": []

    }


    result = app.invoke(
    state,
    config={
        "recursion_limit": 10
      }
    )


    assert len(result["plan"]) > 0

    assert result["execution_status"] == "PASSED"

    assert len(result["screenshots"]) == 1