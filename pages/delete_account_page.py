from playwright.sync_api import Page

class DeleteAccountPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.delete_account_heading = page.get_by_role("heading", name="Account Deleted!")
        self.delete_account_continue_button = page.get_by_test_id("continue-button")

    def click_continue(self):
        self.delete_account_continue_button.click()