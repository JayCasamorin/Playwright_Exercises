from playwright.sync_api import expect, Page
from pages.base_page import BasePage

class BaseProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_name = page.locator(".product-information h2")
        self.product_category = page.locator("p:has-text('Category')")
        self.product_price = page.locator("span > span:has-text('Rs.')")
        self.product_availability = page.locator("p:has-text('Availability')")
        self.product_condition = page.locator("p:has-text('Condition')")
        self.product_brand = page.locator("p:has-text('Brand')")
