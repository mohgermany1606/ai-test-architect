import allure


@allure.title("Search Artificial Intelligence on Wikipedia")
@allure.description(
    "Verify user can search and open AI article"
)
def test_search_ai_article():

    with Browser() as page:

        wiki = WikipediaPage(page)

        wiki.open()

        wiki.search(
            "Artificial Intelligence"
        )

        wiki.verify_article()

        Screenshot.capture(
            page,
            "AI_article"
        )