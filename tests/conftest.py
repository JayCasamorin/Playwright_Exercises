
from playwright.sync_api import Page, Playwright
from pages.home_page import HomePage
import pytest
import re

@pytest.fixture(scope="session", autouse=True)
def set_custom_test_id(playwright: Playwright):
    # Runs once per test session before any browser launches
    playwright.selectors.set_test_id_attribute("data-qa")

@pytest.fixture
def homepage(page: Page) -> HomePage:
    # Block ads: the Google vignette overlay hijacks navigation clicks (notably on WebKit)
    page.route(
        re.compile(r"googlesyndication|doubleclick|googleadservices|adservice\.google"),
        lambda route: route.abort(),
    )
    home_page = HomePage(page)
    home_page.open()
    
    return home_page

