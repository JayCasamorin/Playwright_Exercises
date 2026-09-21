# pages/account_status_page.py
from playwright.sync_api import Page

class AccountStatusPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.account_created_heading = page.get_by_role("heading", name="Account Created!")
        self.account_created_continue_button = page.get_by_test_id("continue-button")

    def click_continue(self):
        self.account_created_continue_button.click()