from playwright.sync_api import Page
from pages.base_page import BasePage

class DeleteAccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Locators
        self.delete_account_heading = page.get_by_role("heading", name="Account Deleted!")
        self.delete_account_continue_button = page.get_by_test_id("continue-button")

    def click_continue(self):
        self.delete_account_continue_button.click()