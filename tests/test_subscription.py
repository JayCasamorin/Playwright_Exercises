from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.cart_page import CartPage
import re

def test_subscription_in_homepage(homepage: HomePage):
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

def test_subscription_in_cart_page(homepage: HomePage):
    # Verify that home page is visible successfully
    expect(
        homepage.home_heading
    ).to_be_visible()

    # Click 'Cart' button
    homepage.navigate_to_cart()
    cartpage = CartPage(homepage.page)

    # verify that cart page is visible successfully
    expect(
        cartpage.page
    ).to_have_url(re.compile(r".*/view_cart"))

    # Scroll down to footer
    cartpage.subscription_heading.scroll_into_view_if_needed()

    # Verify text 'SUBSCRIPTION'
    expect(
        cartpage.subscription_heading
    ).to_be_visible()

    # Enter email address in input and click arrow button
    cartpage.subscribe("test@example.com")

    # Verify success message 'You have been successfully subscribed!' is visible
    expect(
        cartpage.subscribe_success_message
    ).to_be_visible()