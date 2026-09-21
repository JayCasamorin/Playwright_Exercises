# test_register_user.py
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_info_page import AccountInformationPage
from pages.account_status_page import AccountStatusPage
from pages.delete_account_page import DeleteAccountPage


def test_register_user(homepage: HomePage):
    # Verify that home page is visible successfully
    expect(
        homepage.home_header
    ).to_be_visible()

    # Click on 'Signup / Login' button
    homepage.click_signup_login()
    signup_login_page = SignupLoginPage(homepage.page)

    # Verify 'New User Signup!' is visible
    expect(
        signup_login_page.signup_heading
    ).to_be_visible()

    # Enter name and email address
    signup_login_page.enter_name("Jay Casamorin")
    signup_login_page.enter_email("jay.casamorin@gmail.com")

    # Click 'Signup' button
    signup_login_page.click_signup_button()
    account_info_page = AccountInformationPage(homepage.page)

    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    expect(
        account_info_page.account_information_heading
    ).to_be_visible()

    # Fill details: Title, Name, Email, Password, Date of birth
    account_info_page.tick_title("Mr.")
    account_info_page.enter_password("SecurePassword123")
    account_info_page.select_date_of_birth("1", "January", "1990")

    # Select checkbox 'Sign up for our newsletter!'
    # Select checkbox 'Receive special offers from our partners!'
    account_info_page.select_checkboxes(newsletter=True, special_offers=True)

    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    account_info_page.enter_name("Jay", "Casamorin")
    account_info_page.enter_company("OpenAI")
    account_info_page.enter_address("123 Main St", "Apt 4B")
    account_info_page.enter_country("United States")
    account_info_page.enter_state("California")
    account_info_page.enter_city("San Francisco")
    account_info_page.enter_zipcode("1602")
    account_info_page.enter_mobile_number("1234567890")

    # Click 'Create Account button'
    account_info_page.submit_create_account()
    account_status_page = AccountStatusPage(homepage.page)

    # Verify that 'ACCOUNT CREATED!' is visible
    expect(
        account_status_page.account_created_heading
    ).to_be_visible()

    # Click 'Continue' button
    account_status_page.click_continue()

    # Verify that 'Logged in as username' is visible
    expect(
        homepage.logged_in_as_user
    ).to_be_visible()

    # Click 'Delete Account' button
    expect(
        homepage.delete_account_link
    ).to_be_visible()
    homepage.click_delete_account()
    delete_account_page = DeleteAccountPage(homepage.page)

    # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    expect(
        delete_account_page.delete_account_heading
    ).to_be_visible()
    delete_account_page.click_continue()