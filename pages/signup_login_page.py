from playwright.sync_api import Page, expect

class SignupLoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators

        self.signup_heading = page.get_by_role("heading", name="New User Signup!")
        
        self.login_email_input = page.get_by_test_id("login-email")
        self.login_password_input = page.get_by_test_id("login-password")
        self.login_button = page.get_by_test_id("login-button")
        self.error_message = page.get_by_text("Your email or password is incorrect!")

        self.signup_name_input = page.get_by_test_id("signup-name")
        self.signup_email_input = page.get_by_test_id("signup-email")
        self.signup_button = page.get_by_test_id("signup-button")


    def enter_login_email(self, email: str):
        self.login_email_input.fill(email)

    def enter_login_password(self, password: str):
        self.login_password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def enter_signup_name(self, name: str):
        self.signup_name_input.fill(name)

    def enter_signup_email(self, email: str):
        self.signup_email_input.fill(email)

    def click_signup_button(self):
        self.signup_button.click()

    def login(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

    def signup(self, name: str, email: str):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()
    