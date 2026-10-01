from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Locators (home_link inherited from BasePage)
        self.contact_us_heading = page.get_by_role("heading", name="Contact Us")
        self.get_in_touch_heading = page.get_by_role("heading", name="Get In Touch")
        self.name_input = page.get_by_test_id("name")
        self.email_input = page.get_by_test_id("email")
        self.subject_input = page.get_by_test_id("subject")
        self.message_textarea = page.get_by_test_id("message")
        self.upload_file_input = page.locator("input[type='file']")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.success_message = page.locator("#contact-page").get_by_text(
            "Success! Your details have been submitted successfully.",
            exact=True
        )
        self.home_button = page.locator(
            "#contact-page a.btn-success[href='/']"
        )


    def enter_name(self, name: str):
        self.name_input.fill(name)

    def enter_email(self, email: str):
        self.email_input.fill(email)

    def enter_subject(self, subject: str):
        self.subject_input.fill(subject)

    def enter_message(self, message: str):
        self.message_textarea.fill(message)

    def upload_file(self, file_path: str):
        self.upload_file_input.set_input_files(file_path)

    def click_submit(self):
        self.submit_button.click()

    def submit_contact_form(
            self, 
            name: str, 
            email: str, 
            subject: str, 
            message: str,
            file_path: str = None
    ):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_subject(subject)
        self.enter_message(message)
        if file_path:
            self.upload_file(file_path)
        self.click_submit()

    def click_home_button(self):
        self.home_button.click()