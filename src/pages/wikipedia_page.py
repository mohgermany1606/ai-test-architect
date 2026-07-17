class WikipediaPage:


    def __init__(
        self,
        page
    ):

        self.page = page


    def open(self):

        self.page.goto(
            "https://www.wikipedia.org"
        )


    def search(
        self,
        text
    ):

        search_box = self.page.locator(
            "input[name='search']"
        )


        search_box.fill(
            text
        )


        self.page.keyboard.press(
            "Enter"
        )


    def verify_article(self):

        article = self.page.get_by_text(
            "Artificial intelligence"
        ).first


        assert article.is_visible()