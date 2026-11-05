from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def _product_row(self, product_id: int):
        # Create a locator for the product row with the given ID
        return self.page.locator(f"#product-{product_id}")

    def product_in_cart(self, product_id: int):
        # Return the locator for the product row in the cart
        return self._product_row(product_id)

    def product_price(self, product_id: int):
        # Return the locator for the product price in the cart
        return self._product_row(product_id).locator(".cart_price")

    def product_quantity(self, product_id: int):
        # Return the locator for the product quantity in the cart
        return self._product_row(product_id).locator(".cart_quantity")

    def product_total(self, product_id: int):
        # Return the locator for the product total in the cart
        return self._product_row(product_id).locator(".cart_total")
