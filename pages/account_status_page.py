# pages/account_status_page.py
from playwright.sync_api import Page, expect

class AccountStatusPage:
    def __init__(self, page: Page):
        self.page = page
        self.continue_button = page.locator("a[data-qa='continue-button']")

    def verify_heading(self, heading_text: str):
        expect(self.page.get_by_role("heading", name=heading_text)).to_be_visible()

    def click_continue(self):
        self.continue_button.click()