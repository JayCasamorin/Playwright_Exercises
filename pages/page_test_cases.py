from playwright.sync_api import Page
from pages.base_page import BasePage

class PageTestCases(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Locators (home_link inherited from BasePage)
        self.test_cases_heading = page.get_by_role("heading", name="Test Cases", level=2)