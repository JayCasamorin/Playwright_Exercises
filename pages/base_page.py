from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

        # Common locators for all pages can be defined here
        self.home_link = page.get_by_role("link", name="Home")
        self.products_link = page.get_by_role("link", name="Products")
        self.cart_link = page.get_by_role("link", name="Cart")
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")
        self.test_cases_link = page.get_by_role("link", name="Test Cases", exact=True)
        self.api_testing_link = page.get_by_role("link", name="API Testing")
        self.video_tutorials_link = page.get_by_role("link", name="Video Tutorials")
        self.contact_us_link = page.get_by_role("link", name="Contact Us")

    def navigate_to_home(self):
        self.home_link.click()

    def navigate_to_products(self):
        self.products_link.click()

    def navigate_to_cart(self):
        self.cart_link.click()

    def navigate_to_signup_login(self):
        self.signup_login_link.click()

    def navigate_to_test_cases(self):
        self.test_cases_link.click()

    def navigate_to_api_testing(self):
        self.api_testing_link.click()

    def navigate_to_video_tutorials(self):
        self.video_tutorials_link.click()

    def navigate_to_contact_us(self):
        self.contact_us_link.click()