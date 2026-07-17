from playwright.sync_api import sync_playwright
import os


class Browser:


    def __init__(self):
        self.playwright = None
        self.browser = None


    def __enter__(self):

        self.playwright = sync_playwright().start()


        headless = os.getenv(
            "CI",
            "false"
        ) == "true"


        self.browser = self.playwright.chromium.launch(
            headless=headless
        )


        self.page = self.browser.new_page()


        return self.page



    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback
    ):

        self.browser.close()

        self.playwright.stop()