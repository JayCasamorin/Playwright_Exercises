from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.first_product_in_cart = page.locator("#product-1")
        self.first_product_price = page.locator("#product-1 .cart_price")
        self.first_product_quantity = page.locator("#product-1 .cart_quantity")
        self.first_product_total = page.locator("#product-1 .cart_total")

        self.second_product_in_cart = page.locator("#product-2")
        self.second_product_price = page.locator("#product-2 .cart_price")
        self.second_product_quantity = page.locator("#product-2 .cart_quantity")
        self.second_product_total = page.locator("#product-2 .cart_total")
