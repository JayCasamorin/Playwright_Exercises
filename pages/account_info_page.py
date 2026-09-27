# pages/account_info_page.py
from playwright.sync_api import Page, expect # pyright: ignore[reportMissingImports]

class AccountInformationPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators

        self.account_information_heading = page.get_by_role("heading", name="Enter Account Information")
        self.mr_radio = page.get_by_role("radio", name="Mr.")
        self.mrs_radio = page.get_by_role("radio", name="Mrs.")

        self.password_input = page.get_by_role("textbox", name="Password")

        self.days_select = page.get_by_test_id("days")
        self.months_select = page.get_by_test_id("months")
        self.years_select = page.get_by_test_id("years")
        
        self.newsletter_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.special_offers_checkbox = page.get_by_role("checkbox", name="Receive special offers from our partners!")

        self.first_name_input = page.get_by_role("textbox", name="First Name")
        self.last_name_input = page.get_by_role("textbox", name="Last Name")

        self.company_input = page.get_by_test_id("company")

        self.address_input = page.get_by_test_id("address")
        self.address2_input = page.get_by_test_id("address2")
        self.country_select = page.get_by_role("combobox", name="Country")
        self.state_input = page.get_by_role("textbox", name="State")
        self.city_input = page.get_by_role("textbox", name="City")
        self.zipcode_input = page.get_by_test_id("zipcode")

        self.mobile_number_input = page.get_by_role("textbox", name="Mobile Number")

        self.create_account_button = page.get_by_role("button", name="Create Account")

    def tick_title(self, title: str):
        if title == "Mr.":
            self.mr_radio.check()
        elif title == "Mrs.":
            self.mrs_radio.check()

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def select_date_of_birth(self, day: str, month: str, year: str):
        self.days_select.select_option(day)
        self.months_select.select_option(month)
        self.years_select.select_option(year)

    def select_checkboxes(self, newsletter: bool, special_offers: bool):    
        if newsletter:
            self.newsletter_checkbox.check()
        if special_offers:
            self.special_offers_checkbox.check()

    def enter_name(self, first_name: str, last_name: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)

    def enter_company(self, company: str):
        self.company_input.fill(company)

    def enter_address(self, address: str, address2: str):
        self.address_input.fill(address)
        self.address2_input.fill(address2)

    def enter_country(self, country: str):
        self.country_select.select_option(country)

    def enter_state(self, state: str):
        self.state_input.fill(state)

    def enter_city(self, city: str):
        self.city_input.fill(city)

    def enter_zipcode(self, zipcode: str):
        self.zipcode_input.fill(zipcode)

    def enter_mobile_number(self, mobile_number: str):
        self.mobile_number_input.fill(mobile_number)

    def submit_create_account(self):
        self.create_account_button.click()

    def fill_account_info(
            self, title: str, 
            password: str, 
            day: str, 
            month: str, 
            year: str,
            newsletter: bool, 
            special_offers: bool, 
            first_name: str, 
            last_name: str,
            company: str, 
            address: str, 
            address2: str, 
            country: str, 
            state: str,
            city: str, 
            zipcode: str, 
            mobile_number: str
    ):
        self.tick_title(title)
        self.enter_password(password)
        self.select_date_of_birth(day, month, year)
        self.select_checkboxes(newsletter, special_offers)
        self.enter_name(first_name, last_name)
        self.enter_company(company)
        self.enter_address(address, address2)
        self.enter_country(country)
        self.enter_state(state)
        self.enter_city(city)
        self.enter_zipcode(zipcode)
        self.enter_mobile_number(mobile_number)