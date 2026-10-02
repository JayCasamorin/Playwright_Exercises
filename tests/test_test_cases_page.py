from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.page_test_cases import PageTestCases

def test_page_test_cases(homepage: HomePage):
    # Verify that home page is visible successfully
    expect(homepage.home_heading).to_be_visible()

    # Click on 'Test Cases' button
    homepage.navigate_to_test_cases()
    page_test_cases = PageTestCases(homepage.page)

    # Verify user is navigated to test cases page successfully
    expect(page_test_cases.test_cases_heading).to_be_visible()
