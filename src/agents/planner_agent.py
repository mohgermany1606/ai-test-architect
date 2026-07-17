from src.agents.state import AgentState


def planner_agent(
        state: AgentState
) -> AgentState:


    requirement = state["requirement"]


    plan = [

        "Analyze requirement",

        "Generate test scenarios",

        "Execute browser automation",

        "Validate result",

        "Capture evidence"

    ]


    state["plan"] = plan


    return state