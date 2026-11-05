from playwright.sync_api import Page
from pages.base_product_list_page import BaseProductListPage


class ProductsPage(BaseProductListPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.all_products_heading = page.locator(
            ".features_items h2", has_text="All Products"
        )
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")

    def search_product(self, query: str):
        self.search_input.fill(query)
        self.search_button.click()

    def searched_product(self, query: str):
        return self.page.locator(".features_items .col-sm-4", has_text=query)
