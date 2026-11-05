from playwright.sync_api import expect, Page
from pages.base_product_page import BaseProductPage


class BaseProductDetailPage(BaseProductPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_name = page.locator(".product-information h2")
        self.product_category = page.locator("p:has-text('Category')")
        self.product_price = page.locator("span > span:has-text('Rs.')")
        self.add_to_cart_button = page.locator("button:has-text('Add to cart')")
        self.product_availability = page.locator("p:has-text('Availability')")
        self.product_condition = page.locator("p:has-text('Condition')")
        self.product_brand = page.locator("p:has-text('Brand')")

    def set_quantity(self, quantity: int):
        quantity_input = self.page.locator("#quantity")
        quantity_input.fill(str(quantity))

    def add_to_cart(self):
        # The click is silently ignored if it lands before the page JS handler attaches
        self.page.wait_for_load_state("networkidle")
        self.add_to_cart_button.click()