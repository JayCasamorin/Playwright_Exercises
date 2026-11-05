from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.base_product_detail_page import BaseProductDetailPage
import re

def navigate_to_products_page(homepage: HomePage):
    # Verify that home page is visible successfully
    expect(
        homepage.home_heading
    ).to_be_visible()

    # Click on 'Products' button
    homepage.navigate_to_products()
    products_page = ProductsPage(homepage.page)

    # Verify user is navigated to ALL PRODUCTS page successfully
    expect(
        products_page.all_products_heading
    ).to_be_visible()

    # The products list is visible
    expect(
            products_page.products_list
    ).to_be_visible()
    return products_page

def test_verify_products(homepage: HomePage):
    products_page = navigate_to_products_page(homepage)

    # Click on 'View Product' of first product
    products_page.view_product(product_id=1)
    product_details = BaseProductDetailPage(products_page.page)

    # User is landed to product detail page
    expect(
        product_details.page
    ).to_have_url(re.compile(r".*/product_details/.*"))

    # Verify that detail detail is visible: product name, category, price, availability, condition, brand
    expect(
        product_details.product_name
    ).to_be_visible()
    expect(
        product_details.product_category
    ).to_be_visible()
    expect(
        product_details.product_price
    ).to_be_visible()
    expect(
        product_details.product_availability
    ).to_be_visible()
    expect(
        product_details.product_condition
    ).to_be_visible()
    expect(
        product_details.product_brand
    ).to_be_visible()

def test_search_product(homepage: HomePage):
    products_page = navigate_to_products_page(homepage)

    # Search for a product
    search_query = "top"
    products_page.search_product(search_query)

    # Verify that the searched product is visible in the results
    expect(
        products_page.searched_product(search_query)
    ).not_to_have_count(0)

def test_add_to_cart(homepage: HomePage):
    products_page = navigate_to_products_page(homepage)

    # Hover over first product and click 'Add to cart'
    products_page.add_product_to_cart(product_id=1)

    # Click 'Continue Shopping' button
    products_page.continue_shopping()

    # Hover over second product and click 'Add to cart'
    products_page.add_product_to_cart(product_id=2)

    # Click 'View Cart' button
    products_page.view_cart()
    cart_page = CartPage(products_page.page)

    # Verify both products are added to Cart
    expect(
        cart_page.product_in_cart(product_id=1)
    ).to_be_visible()
    
    expect(
        cart_page.product_in_cart(product_id=2)
    ).to_be_visible()

    # Verify their prices, quantity and total price
    expect(
        cart_page.product_price(product_id=1)
    ).to_be_visible()
    expect(
        cart_page.product_quantity(product_id=1)
    ).to_be_visible()
    expect(
        cart_page.product_total(product_id=1)
    ).to_be_visible()

    expect(
        cart_page.product_price(product_id=2)
    ).to_be_visible()
    expect(
        cart_page.product_quantity(product_id=2)
    ).to_be_visible()
    expect(
        cart_page.product_total(product_id=2)
    ).to_be_visible()

def test_verify_product_quantity_in_cart(homepage: HomePage):
    # Verify that home page is visible successfully
    expect(
        homepage.home_heading
    ).to_be_visible()

    # Click 'View Product' for any product on home page
    homepage.view_product(product_id=1)
    product_details = BaseProductDetailPage(homepage.page)

    # Verify product detail is opened
    expect(
        product_details.product_name
    ).to_be_visible()

    # Increase quantity to 4
    product_details.set_quantity(4)

    # Click 'Add to cart' button
    product_details.add_to_cart()

    # Click 'View Cart' button
    product_details.view_cart()
    cart_page = CartPage(product_details.page)

    # Verify that product is displayed in cart page with exact quantity
    expect(
        cart_page.product_in_cart(product_id=1)
    ).to_be_visible()
    expect(
        cart_page.product_quantity(product_id=1)
    ).to_have_text("4")

