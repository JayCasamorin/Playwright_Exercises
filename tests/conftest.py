
from playwright.sync_api import Page, Playwright
from pages.home_page import HomePage
import pytest

@pytest.fixture(scope="session", autouse=True)
def set_custom_test_id(playwright: Playwright):
    # Runs once per test session before any browser launches
    playwright.selectors.set_test_id_attribute("data-qa")

@pytest.fixture
def homepage(page: Page) -> HomePage:
    home_page = HomePage(page)
    home_page.open()
    
    return home_page

