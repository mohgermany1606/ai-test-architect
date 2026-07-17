from playwright.sync_api import sync_playwright


class Browser:

    def __init__(self):
        self.playwright = None
        self.browser = None


    def __enter__(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=True
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