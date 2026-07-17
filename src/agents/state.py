from typing import TypedDict, List


class AgentState(TypedDict):

    requirement: str

    plan: List[str]

    test_cases: List[dict]

    execution_result: str

    execution_status: str

    screenshots: List[str]

    analysis: str
    
    suggestion: str