from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage

def test_login_user_successful(homepage: HomePage):
    user_name = "Jay Casamorin"
    
    # Verify that home page is visible successfully
    expect(
        homepage.home_header
    ).to_be_visible()

    # Click on 'Signup / Login' button
    homepage.click_signup_login()
    signup_login_page = SignupLoginPage(homepage.page)

    # Verify 'Login to your account' is visible
    expect(
        signup_login_page.login_heading
    ).to_be_visible()

    # Enter correct email address and password
    signup_login_page.login_email_input.fill("casamorin.jay@gmail.com")
    signup_login_page.login_password_input.fill("SecurePassword123")

    # Click 'login' button
    signup_login_page.login_button.click()

    # Verify that user is logged in successfully
    expect(
        homepage.logged_in_as_user
    ).to_have_text(f"Logged in as {user_name}")

def test_login_user_incorrect_credentials(homepage: HomePage):
    # Verify that home page is visible successfully
    expect(
        homepage.home_header
    ).to_be_visible()

    # Click on 'Signup / Login' button
    homepage.click_signup_login()
    signup_login_page = SignupLoginPage(homepage.page)

    # Verify 'Login to your account' is visible
    expect(
        signup_login_page.signup_heading
    ).to_be_visible()

    # Enter incorrect email address and password
    signup_login_page.login_email_input.fill("incorrect_email@example.com")
    signup_login_page.login_password_input.fill("wrong_password")


    # Click 'login' button
    signup_login_page.login_button.click()

    # Verify error 'Your email or password is incorrect!' is visible
    expect(
        signup_login_page.error_message
    ).to_be_visible()

    

