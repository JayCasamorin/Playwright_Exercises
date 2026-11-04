from playwright.sync_api import expect
from pages.home_page import HomePage

def test_subscription(homepage: HomePage):
    # Verify that home page is visible successfully
    expect(
        homepage.home_heading
    ).to_be_visible()

    # Scroll down to footer
    homepage.subscription_heading.scroll_into_view_if_needed()

    # Verify text 'SUBSCRIPTION'
    expect(
        homepage.subscription_heading
    ).to_be_visible()

    # Enter email address in input and click arrow button
    homepage.subscribe("test@example.com")

    # Verify success message 'You have been successfully subscribed!' is visible
    expect(
        homepage.subscribe_success_message
    ).to_be_visible()
