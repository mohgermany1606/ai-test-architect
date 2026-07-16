class WikipediaPage:

    def __init__(self,page):
        self.page = page


    def open(self):

        self.page.goto(
            "https://wikipedia.org"
        )


    def search(self,keyword):

        self.page.locator(
            "input[name='search']"
        ).fill(keyword)

        self.page.keyboard.press("Enter")


    def verify_article(self):

        self.page.locator(
            "#firstHeading"
        ).wait_for()