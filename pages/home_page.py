from playwright.sync_api import Page, expect
from pages.base_page import BasePage

URL = "https://automationexercise.com/"
class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Locators (signup_login_link / contact_us_link inherited from BasePage)
        self.home_header = page.get_by_alt_text("Website for automation practice")
        self.logged_in_as_user = page.get_by_role('listitem').filter(has_text=f"Logged in as")
        self.delete_account_link = page.get_by_role("link",name="Delete Account")
        self.logout_button = page.get_by_role("link", name="Logout")


    def open(self):
        self.page.goto(URL)

    def click_signup_login(self):
        self.signup_login_link.click()

    def click_delete_account(self):
        self.delete_account_link.click()

    def click_logout(self):
        self.logout_button.click()

    def click_contact_us(self):
        self.contact_us_link.click()