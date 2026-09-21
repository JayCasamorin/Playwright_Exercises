from playwright.sync_api import Page, expect

class SignupLoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators

        self.signup_heading = page.get_by_role("heading", name="New User Signup!")
        self.name_input = page.get_by_role("textbox", name="Name")
        self.email_input = page.get_by_test_id("signup-email")
        self.signup_button = page.get_by_role("button", name="Signup")

    def enter_name(self, name: str):
        self.name_input.fill(name)

    def enter_email(self, email: str):
        self.email_input.fill(email)

    def click_signup_button(self):
        self.signup_button.click()

    def signup(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()
    