"""
BasePage module: provides common actions for Playwright page objects.
All methods expect Locator objects for reliable interactions.
"""

import allure
from playwright.sync_api import Locator, Page


class BasePage:
    """Base class for page objects with common actions."""

    def __init__(self, page: Page, base_url: str = "") -> None:
        """Initialize with Playwright page and optional base URL."""
        self.page = page
        self.base_url = base_url

    @allure.step("Go to page: {path}")
    def goto(self, path: str = "/", timeout: int = 30000) -> None:
        """Navigate to a URL path."""
        self.page.goto(
         self.base_url + path,
         wait_until="load",
         timeout=timeout
        )

    @allure.step("Click element")
    def click(self, locator: Locator) -> None:
        """Wait for element and click."""
        locator.wait_for(state="visible", timeout=20000)
        locator.click()

    @allure.step("Fill element with text: {text}")
    def fill(self, locator: Locator, text: str) -> None:
        """Wait for element and fill text."""
        locator.wait_for(state="visible")
        locator.fill(text)

    @allure.step("Get text from element")
    def get_text(self, locator: Locator) -> str:
        """Return trimmed inner text of element."""
        locator.wait_for(state="visible")
        return locator.inner_text().strip()

    @allure.step("Get value from input")
    def get_value(self, locator: Locator) -> str:
        """Return value of input element."""
        locator.wait_for(state="visible")
        return locator.input_value()

    @allure.step("Check visibility of element")
    def is_visible(self, locator: Locator) -> bool:
        """Return True if element is visible."""
        locator.wait_for(state="visible")
        return locator.is_visible()

    @allure.step("Check checkbox")
    def check(self, locator: Locator) -> None:
        """Check checkbox if not checked."""
        locator.wait_for(state="visible")
        if not locator.is_checked():
            locator.check()

    @allure.step("Uncheck checkbox")
    def uncheck(self, locator: Locator) -> None:
        """Uncheck checkbox if checked."""
        locator.wait_for(state="visible")
        if locator.is_checked():
            locator.uncheck()

    @allure.step("Verify if checkbox is checked")
    def is_checked(self, locator: Locator) -> bool:
        """Return True if checkbox is checked."""
        locator.wait_for(state="visible")
        return locator.is_checked()

    @allure.step("Select option '{value}' from dropdown")
    def select_option(self, locator: Locator, value: str) -> None:
        """Select a value from dropdown."""
        locator.wait_for(state="visible")
        locator.select_option(value)
