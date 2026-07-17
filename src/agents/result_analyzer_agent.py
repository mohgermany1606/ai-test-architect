from src.agents.state import AgentState


def result_analyzer_agent(
    state: AgentState
) -> AgentState:


    if state["execution_status"] == "PASSED":

        state["execution_result"] = (
            "Test execution successful. "
            "No issues detected."
        )

    else:

        state["execution_result"] = (
            "Test execution failed. "
            "Investigation required."
        )


    return state