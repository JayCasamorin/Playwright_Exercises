from playwright.sync_api import Page
from pages.base_page import BasePage


class BaseProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_modal = page.locator("#cartModal")
        self.cart_modal_view_cart_button = page.locator(
            "#cartModal .modal-body a[href*='/view_cart']"
        )
        self.cart_modal_continue_shopping_button = page.locator(
            "#cartModal .modal-footer button.btn-success"
        )

    def continue_shopping(self):
        self.cart_modal_continue_shopping_button.click()

    def view_cart(self):
        self.cart_modal_view_cart_button.click()
