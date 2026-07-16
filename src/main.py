from browser import Browser
from wikipedia import Wikipedia


def main():

    with Browser() as page:

        wiki = Wikipedia(page)

        wiki.open()

        wiki.search("Artificial Intelligence")

        wiki.open_article()

        wiki.take_screenshot()


if __name__ == "__main__":
    main()