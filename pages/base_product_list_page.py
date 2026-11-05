from playwright.sync_api import Page
from pages.base_product_page import BaseProductPage


class BaseProductListPage(BaseProductPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.products_list = page.locator(".features_items")

    def _product_by_id(self, product_id: int):
        # Create locators for the product with the given ID
        return self.products_list.locator(
            f".col-sm-4:has(.add-to-cart[data-product-id='{product_id}'])"
        )

    def view_product(self, product_id: int):
        self._product_by_id(product_id).locator(
            "a[href*='/product_details/']"
        ).click()

    def add_product_to_cart(self, product_id: int):
        product = self._product_by_id(product_id)
        product.hover()
        product.locator(".product-overlay a.add-to-cart").click()
