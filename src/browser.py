from playwright.sync_api import sync_playwright

from src.config_reader import ConfigReader
from src.utils.logger import get_logger


class Browser:

    logger = get_logger(__name__)

    def __enter__(self):

        self.logger.info("Starting browser")

        config = ConfigReader.load()

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=config["browser"]["headless"]
        )

        self.page = self.browser.new_page()

        self.logger.info("Browser started successfully")

        return self.page


    def __exit__(self, exc_type, exc_value, traceback):

        self.logger.info("Closing browser")

        self.browser.close()

        self.playwright.stop()