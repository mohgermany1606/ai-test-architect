from src.agents.state import AgentState


def failure_analyzer_agent(
    state: AgentState
) -> AgentState:


    if state["execution_status"] == "FAILED":

        error = state["execution_result"]


        print(
            "Analyzing failure:"
        )

        print(error)


        state["analysis"] = (
            "Failure caused by locator or UI change"
        )


        state["suggestion"] = (
            "Review locator and retry execution"
        )


    return state