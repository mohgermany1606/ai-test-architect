from src.agents.state import AgentState
from src.ai.test_generator import TestGenerator


def generate_tests_agent(state: AgentState) -> AgentState:


    requirement = state["requirement"]


    tests = TestGenerator.generate(
        requirement
    )


    state["test_cases"] = tests


    return state