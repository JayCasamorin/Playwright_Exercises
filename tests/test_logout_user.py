from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage

def test_logout_user(homepage: HomePage):
    user_name = "Jay Casamorin"
    user_email = "casamorin.jay@gmail.com"
    user_password = "SecurePassword123"

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
    signup_login_page.login(user_email, user_password)

    # Verify that 'Logged in as username' is visible
    expect(
        homepage.logged_in_as_user
    ).to_have_text(f"Logged in as {user_name}")

    # Click on 'Logout' button
    homepage.click_logout()

    # Verify that user is navigated to login page
    expect(
        signup_login_page.login_heading
    ).to_be_visible()