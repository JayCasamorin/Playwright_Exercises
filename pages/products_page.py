from playwright.sync_api import expect, Page
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.all_products_heading = page.locator(".features_items h2", has_text="All Products")        
        self.products_list = page.locator(".features_items")
        self.view_first_product_button = page.locator(".features_items .col-sm-4").first.locator("a[href*='/product_details/']")
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")

    def view_first_product(self):
        self.view_first_product_button.click()

    def search_product(self, query: str):
        self.search_input.fill(query)
        self.search_button.click()

    def searched_product(self, query: str):
        return self.page.locator(".features_items .col-sm-4", has_text=query)