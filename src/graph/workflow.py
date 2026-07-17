from langgraph.graph import StateGraph, END

from src.agents.state import AgentState

from src.agents.planner_agent import planner_agent
from src.agents.test_generation_agent import generate_tests_agent
from src.agents.execution_agent import execution_agent
from src.agents.result_analyzer_agent import result_analyzer_agent
from src.agents.failure_analyzer_agent import failure_analyzer_agent


def create_workflow():

    workflow = StateGraph(AgentState)


    # Nodes

    workflow.add_node(
        "planner",
        planner_agent
    )


    workflow.add_node(
        "generator",
        generate_tests_agent
    )


    workflow.add_node(
        "executor",
        execution_agent
    )


    workflow.add_node(
        "analyzer",
        result_analyzer_agent
    )


    workflow.add_node(
        "failure_analyzer",
        failure_analyzer_agent
    )


    # Entry point

    workflow.set_entry_point(
        "planner"
    )


    # Flow

    workflow.add_edge(
        "planner",
        "generator"
    )


    workflow.add_edge(
        "generator",
        "executor"
    )


    workflow.add_edge(
        "executor",
        "analyzer"
    )


    workflow.add_edge(
        "analyzer",
        "failure_analyzer"
    )


    workflow.add_edge(
        "failure_analyzer",
        END
    )


    return workflow.compile(
    debug=False
    )