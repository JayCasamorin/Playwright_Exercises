from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.signup_login_link = page.locator("a[href='/login']")
        self.logged_in_as_user = page.get_by_role('listitem').filter(has_text="Logged in as")
        self.delete_account_link = page.locator("a[href='/delete_account']")

    def navigate(self, url: str = "https://automationexercise.com/"):
        self.page.goto(url)
        expect(self.page).to_have_title("Automation Exercise")

    def click_signup_login(self):
        self.signup_login_link.click()

    def verify_logged_in_as(self, username: str):
        expect(self.page.get_by_role("listitem").filter(has_text=f"Logged in as {username}")).to_be_visible()

    def click_delete_account(self):
        self.delete_account_link.click()