import allure

from src.browser import Browser
from src.pages.wikipedia_page import WikipediaPage



@allure.title(
    "Search Artificial Intelligence on Wikipedia"
)
@allure.description(
    "Verify user can search and open AI article"
)
def test_search_ai_article():


    with Browser() as page:


        wiki = WikipediaPage(
            page
        )


        wiki.open()


        wiki.search(
            "Artificial Intelligence"
        )


def verify_article(self):

    heading = self.page.locator(
        "#firstHeading"
    )

    heading.wait_for(
        state="visible"
    )


    assert (
        "Artificial intelligence"
        in heading.inner_text()
    )