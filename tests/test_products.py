from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.base_product_detail_page import BaseProductDetailPage
import re

def test_verify_products(homepage: HomePage):
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

    # Click on 'View Product' of first product
    products_page.view_first_product()
    product_details = BaseProductDetailPage(homepage.page)

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

    # Search for a product
    search_query = "top"
    products_page.search_product(search_query)

    # Verify that the searched product is visible in the results
    expect(
        products_page.searched_product(search_query)
    ).not_to_have_count(0)