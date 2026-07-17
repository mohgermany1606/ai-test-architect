from src.memory.locator_memory import locator_memory


class BrowserTool:

    def open_website(self, page, url):

        page.goto(url)

    def enter_text(
        self,
        page,
        element,
        locator,
        text
    ):

        saved_locator = locator_memory.get_locator(
            element
        )

        if saved_locator:

            print(
                "Using memory locator:",
                saved_locator
            )

            locator = saved_locator

        else:

            print(
                "Saving new locator:",
                locator
            )

            locator_memory.save_locator(
                element,
                locator
            )

        page.locator(
            locator
        ).fill(
            text
        )

    def press_enter(self, page):

        page.keyboard.press(
            "Enter"
        )

    def take_screenshot(
        self,
        page,
        path
    ):

        page.screenshot(
            path=path
        )


browser_tool = BrowserTool()