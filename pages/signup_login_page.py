from playwright.sync_api import Page, expect

class SignupLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_heading = page.get_by_role("heading", name="New User Signup!")
        self.name_input = page.locator("input[data-qa='signup-name']")
        self.email_input = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")

    def verify_on_signup_page(self):
        expect(self.page).to_have_url("https://automationexercise.com/login")
        expect(self.signup_heading).to_be_visible()

    def signup(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()
    