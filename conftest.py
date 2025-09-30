import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture(scope="session")
def base_url():
    """
    Base URL for the application under test.
    """
    return "https://automationexercise.com"


@pytest.fixture(scope="session")
def browser(browser_name):
    """
    Launches the Playwright browser based on the selected browser name.
    """
    with sync_playwright() as p:
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=True)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=True)
        else:
            browser = p.webkit.launch(headless=True)

        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """
    Creates a new browser context and page for each test function.
    """
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def login_signup_page(page, base_url):
    """
    Fixture to navigate to the Signup/Login page.
    Returns a tuple of (HomePage, LoginPage) objects.
    """
    home = HomePage(page, base_url)

    home.goto("/")

    home.go_to_signup_or_login()

    return LoginPage(page, base_url)


@pytest.fixture
def products_page(page, base_url):
    """
    Fixture to navigate to the Products page
    """
    home = HomePage(page, base_url)
    home.goto("/")
    home.go_to_products_page()
    return ProductsPage(page, base_url)


@pytest.fixture
def login_user(login_signup_page):
    """
    Fixture to log in a user and verify successful login.

    """
    def _login(email: str, password: str, username: str):
        login_signup_page.fill_login_form(email, password)
        login_signup_page.click_login_button()
        login_signup_page.verify_logged_in_user(username)
        return login_signup_page

    return _login
