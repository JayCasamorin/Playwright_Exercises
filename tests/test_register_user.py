# test_register_user.py
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_info_page import AccountInformationPage
from pages.account_status_page import AccountStatusPage
from pages.delete_account_page import DeleteAccountPage


def test_register_user(homepage: HomePage):
    # Load Data
    user_name = ("Jay" , "Casamorin")
    user_email = "jay.casamorin@gmail.com"
    user_title = "Mr."
    user_password = "SecurePassword123"
    user_date_of_birth = ("1", "January", "1990")
    user_company = "OpenAI"
    user_address = ("123 Main St", "Apt 4B")
    user_country = "United States"
    user_state = "California"
    user_city = "San Francisco"
    user_zipcode = "1602"
    user_mobile_number = "1234567890"
    
    # Verify that home page is visible successfully
    expect(
        homepage.home_heading
    ).to_be_visible()

    # Click on 'Signup / Login' button
    homepage.click_signup_login()
    signup_login_page = SignupLoginPage(homepage.page)
    
    # Verify 'New User Signup!' is visible
    expect(
        signup_login_page.signup_heading
    ).to_be_visible()

    # Enter name and email address
    signup_login_page.signup_name_input.fill(" ".join(user_name))
    signup_login_page.signup_email_input.fill(user_email)

    # Click 'Signup' button
    signup_login_page.click_signup_button()
    account_info_page = AccountInformationPage(homepage.page)

    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    expect(
        account_info_page.account_information_heading
    ).to_be_visible()

    # Fill details: Title, Name, Email, Password, Date of birth
    account_info_page.tick_title(user_title)
    account_info_page.enter_password(user_password)
    account_info_page.select_date_of_birth(*user_date_of_birth)

    # Select checkbox 'Sign up for our newsletter!'
    # Select checkbox 'Receive special offers from our partners!'
    account_info_page.select_checkboxes(newsletter=True, special_offers=True)

    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    account_info_page.enter_name(*user_name)
    account_info_page.enter_company(user_company)
    account_info_page.enter_address(*user_address)
    account_info_page.enter_country(user_country)
    account_info_page.enter_state(user_state)
    account_info_page.enter_city(user_city)
    account_info_page.enter_zipcode(user_zipcode)
    account_info_page.enter_mobile_number(user_mobile_number)

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
        ).to_have_text(f"Logged in as {' '.join(user_name)}")

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

def test_register_user_existing_email(homepage: HomePage):
    # Load Data
    user_name = "Jay Casamorin"
    user_email = "casamorin.jay@gmail.com"

    # Verify that home page is visible successfully
    expect(
        homepage.home_heading
    ).to_be_visible()

    # Click on 'Signup / Login' button
    homepage.click_signup_login()
    signup_login_page = SignupLoginPage(homepage.page)

    # Enter name and already registered email address
    signup_login_page.enter_signup_name(user_name)
    signup_login_page.enter_signup_email(user_email)

    # Click 'Signup' button
    signup_login_page.click_signup_button()

    # Verify error message for existing email
    expect(
        signup_login_page.existing_email_error
    ).to_be_visible()