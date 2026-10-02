from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage

def test_contact_us_form_submission(homepage: HomePage):
    # Load test data
    user_name = "Jay Casamorin"
    user_email = "casamorin.jay@gmail.com"
    user_subject = "Test Subject"
    user_message = "This is a test message."
    user_file_path = "test_files/test_file.txt"

    # Auto-click OK when the alert appears
    homepage.page.on("dialog", lambda dialog: dialog.accept())

    # Verify that home page is visible successfully
    expect(
        homepage.home_heading
    ).to_be_visible()

    # Navigate to 'Contact Us' page
    homepage.click_contact_us()
    contact_us_page = ContactUsPage(homepage.page)
    
    # Verify 'GET IN TOUCH' is visible
    expect(
        contact_us_page.get_in_touch_heading
    ).to_be_visible()

    # Fill and submit the contact us form
    contact_us_page.submit_contact_form(
        name=user_name,
        email=user_email,
        subject=user_subject,
        message=user_message,
        file_path=user_file_path
    )

    # Verify success message 'Success! Your details have been submitted successfully.' is visible
    expect(
        contact_us_page.success_message
    ).to_be_visible()

    # Click 'Home' button and verify that landed to home page successfully
    contact_us_page.click_home_button()
    expect(
        homepage.home_heading
    ).to_be_visible()


