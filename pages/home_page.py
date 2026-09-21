from playwright.sync_api import Page, expect

URL = "https://automationexercise.com/"
class HomePage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.home_header = page.get_by_alt_text("Website for automation practice")
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")
        self.logged_in_as_user = page.get_by_role('listitem').filter(has_text=f"Logged in as")
        self.delete_account_link = page.get_by_role("listitem").filter(has_text="Delete Account")

    def open(self):
        self.page.goto(URL)

    def click_signup_login(self):
        self.signup_login_link.click()

    def click_delete_account(self):
        self.delete_account_link.click()