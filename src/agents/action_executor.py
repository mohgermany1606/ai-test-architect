import re


def extract_text(action):

    match = re.search(
        r"'(.*?)'",
        action
    )

    if match:
        return match.group(1)

    return "Artificial Intelligence"



def execute_action(page, action):

    action_lower = action.lower()


    if (
        "wikipedia" in action_lower
        or "navigate" in action_lower
        or "open" in action_lower
    ):

        page.goto(
            "https://wikipedia.org"
        )


    elif (
        "search" in action_lower
        or "enter the term" in action_lower
    ):

        search_text = extract_text(action)

        print(
            "Searching:",
            search_text
        )


        page.locator(
            "input[name='search']"
        ).fill(
            search_text
        )


    elif (
        "submit" in action_lower
        or "enter" in action_lower
        or "click" in action_lower
    ):

        page.keyboard.press(
            "Enter"
        )


    else:

        print(
            "Unknown action:",
            action
        )