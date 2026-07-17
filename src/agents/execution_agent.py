from src.agents.state import AgentState
from src.agents.action_executor import execute_action
from src.browser import Browser



def execution_agent(
    state: AgentState
) -> AgentState:


    try:

        with Browser() as page:


            test_case = state["test_cases"][0]


            for step in test_case.steps:

                print(
                    "Executing:",
                    step
                )

                execute_action(
                    page,
                    step
                )


            screenshot_path = (
                "screenshots/ai_article.png"
            )


            page.screenshot(
                path=screenshot_path
            )


            state["execution_status"] = "PASSED"


            state["execution_result"] = (
                "Test executed successfully"
            )


            state["screenshots"].append(
                screenshot_path
            )


    except Exception as error:


        print(
            "EXECUTION ERROR:",
            error
        )


        state["execution_status"] = "FAILED"

        state["execution_result"] = str(error)


    return state