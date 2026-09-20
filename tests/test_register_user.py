# test_register_user.py
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_info_page import AccountInformationPage
from pages.account_status_page import AccountStatusPage


def test_register_user(page: Page):
    # Initialize Page Objects
    home_page = HomePage(page)
    signup_login_page = SignupLoginPage(page)
    account_info_page = AccountInformationPage(page)
    status_page = AccountStatusPage(page)

    # 1. Navigate to Home & click Signup/Login
    home_page.navigate("https://automationexercise.com/")
    home_page.click_signup_login()

    # 2. Complete initial Signup
    signup_login_page.verify_on_signup_page()
    signup_login_page.signup("Jay Casamorin", "jay.casamorin@gmail.com")

    # 3. Complete Form Details
    account_info_page.verify_page_loaded()
    account_info_page.fill_account_details(
        password="jaycasamorin",
        day="17",
        month="12",
        year="1999"
    )
    account_info_page.select_checkboxes(newsletter=True, special_offers=True)
    
    address_details = {
        "first_name": "Jay",
        "last_name": "Casamorin",
        "company": "Example Company",
        "address": "123 Main St",
        "address2": "Apt 4B",
        "country": "Canada",
        "state": "Ontario",
        "city": "Toronto",
        "zipcode": "M5H 2N2",
        "mobile_number": "+1 416-555-1234"
    }
    account_info_page.fill_address_information(address_details)
    account_info_page.submit_account_creation()

    # 4. Verify Account Creation
    status_page.verify_heading("Account Created!")
    status_page.click_continue()

    # 5. Verify Login Status & Delete Account
    home_page.verify_logged_in_as("Jay Casamorin")
    home_page.click_delete_account()

    # 6. Verify Account Deletion
    status_page.verify_heading("Account Deleted!")
    status_page.click_continue()