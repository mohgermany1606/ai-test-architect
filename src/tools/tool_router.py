from src.tools.browser_tool import browser_tool


def execute_tool(
    page,
    action
):

    action_lower = action.lower()


    if (
        "wikipedia" in action_lower
        or "navigate" in action_lower
        or "open" in action_lower
    ):

        browser_tool.open_website(
            page,
            "https://wikipedia.org"
        )


    elif (
        "search" in action_lower
        or "enter" in action_lower
    ):

        browser_tool.enter_text(
            page,
            "search_box",
            "input[name='search']",
            "AI"
        )


    elif (
        "submit" in action_lower
        or "press enter" in action_lower
    ):

        browser_tool.press_enter(
            page
        )


    else:

        print(
            "No tool found for:",
            action
        )   