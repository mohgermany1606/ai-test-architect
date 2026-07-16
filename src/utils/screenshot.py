from pathlib import Path
import allure


class Screenshot:

    @staticmethod
    def capture(page, name):

        Path("screenshots").mkdir(
            exist_ok=True
        )

        screenshot_path = f"screenshots/{name}.png"

        page.screenshot(
            path=screenshot_path,
            full_page=True
        )

        allure.attach.file(
            screenshot_path,
            name,
            attachment_type=allure.attachment_type.PNG
        )