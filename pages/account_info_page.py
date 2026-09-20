# pages/account_info_page.py
from playwright.sync_api import Page, expect

class AccountInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Enter Account Information")
        self.mr_radio = page.get_by_role("radio", name="Mr.")
        self.password_input = page.locator("input[data-qa='password']")
        self.days_select = page.locator("select[data-qa='days']")
        self.months_select = page.locator("select[data-qa='months']")
        self.years_select = page.locator("select[data-qa='years']")
        
        self.newsletter_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.optin_checkbox = page.get_by_role("checkbox", name="Receive special offers from our partners!")

        self.first_name_input = page.locator("input[data-qa='first_name']")
        self.last_name_input = page.locator("input[data-qa='last_name']")
        self.company_input = page.locator("input[data-qa='company']")
        self.address_input = page.locator("input[data-qa='address']")
        self.address2_input = page.locator("input[data-qa='address2']")
        self.country_select = page.get_by_role("combobox", name="Country")
        self.state_input = page.locator("input[data-qa='state']")
        self.city_input = page.locator("input[data-qa='city']")
        self.zipcode_input = page.locator("input[data-qa='zipcode']")
        self.mobile_number_input = page.locator("input[data-qa='mobile_number']")
        self.create_account_button = page.locator("button[data-qa='create-account']")

    def verify_page_loaded(self):
        expect(self.heading).to_be_visible()

    def fill_account_details(self, password: str, day: str, month: str, year: str, title: str = "Mr."):
        if title == "Mr.":
            self.mr_radio.check()
        self.password_input.fill(password)
        self.days_select.select_option(day)
        self.months_select.select_option(month)
        self.years_select.select_option(year)

    def select_checkboxes(self, newsletter: bool = True, special_offers: bool = True):
        if newsletter:
            self.newsletter_checkbox.check()
        if special_offers:
            self.optin_checkbox.check()

    def fill_address_information(self, details: dict):
        self.first_name_input.fill(details.get("first_name", ""))
        self.last_name_input.fill(details.get("last_name", ""))
        self.company_input.fill(details.get("company", ""))
        self.address_input.fill(details.get("address", ""))
        self.address2_input.fill(details.get("address2", ""))
        self.country_select.select_option(details.get("country", "United States"))
        self.state_input.fill(details.get("state", ""))
        self.city_input.fill(details.get("city", ""))
        self.zipcode_input.fill(details.get("zipcode", ""))
        self.mobile_number_input.fill(details.get("mobile_number", ""))

    def submit_account_creation(self):
        self.create_account_button.click()