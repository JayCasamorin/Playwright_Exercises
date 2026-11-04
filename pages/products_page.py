from playwright.sync_api import expect, Page
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.all_products_heading = page.locator(".features_items h2", has_text="All Products")        
        self.products_list = page.locator(".features_items")
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")

        self.cart_modal = page.locator("#cartModal")
        self.cart_modal_view_cart_button = page.locator("#cartModal .modal-body a[href*='/view_cart']")
        self.cart_modal_continue_shopping_button = page.locator("#cartModal .modal-footer button.btn-success")

        self.first_product = page.locator(".single-products").first
        self.first_product_view_button = page.locator(".features_items .col-sm-4").first.locator("a[href*='/product_details/']")
        self.first_product_add_to_cart_button_hover = page.locator(".product-overlay a.add-to-cart[data-product-id='1']")

        self.second_product = page.locator(".single-products").nth(1)
        self.second_product_add_to_cart_button_hover = page.locator(".product-overlay a.add-to-cart[data-product-id='2']")

    def view_first_product(self):
        self.first_product_view_button.click()

    def search_product(self, query: str):
        self.search_input.fill(query)
        self.search_button.click()

    def searched_product(self, query: str):
        return self.page.locator(".features_items .col-sm-4", has_text=query)

    def add_product_to_cart(self, product_id: int):
        product = self.products_list.locator(
            f".col-sm-4:has(.add-to-cart[data-product-id='{product_id}'])"
        )
        product.hover()
        product.locator(".product-overlay a.add-to-cart").click()

    def continue_shopping(self):
        self.cart_modal_continue_shopping_button.click()

    def view_cart(self):
        self.cart_modal_view_cart_button.click()
        
