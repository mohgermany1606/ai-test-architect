from pathlib import Path


class Wikipedia:

    URL = "https://wikipedia.org"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def search(self, text):

        self.page.locator("input[name='search']").fill(text)

        self.page.keyboard.press("Enter")

    def open_article(self):

        self.page.locator("#firstHeading").wait_for()

    def take_screenshot(self):

        Path("screenshots").mkdir(exist_ok=True)

        self.page.screenshot(
            path="screenshots/artificial_intelligence.png",
            full_page=True
        )