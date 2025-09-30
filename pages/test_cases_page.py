"""
    Page object for the Test cases Page.
"""
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class CasesPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        """
        Provides methods to interact with the Test cases page elements.
        """
        super().__init__(page, base_url)
        self.page = page
        self.verify_login_to_account_text = page.locator(
            'h2.title.text-center b'
        )

    @allure.step("Verify 'Test Cases' text is visible")
    def verify_test_cases_text(self, expected_text: str):
        """
        Verify 'Test Cases' text is visible.
        """
        self.verify_login_to_account_text.wait_for(
            state="visible",
            timeout=10000
        )
        actual_text = self.verify_login_to_account_text.text_content()
        assert actual_text.strip() == expected_text, (
            f"Expected '{expected_text}' "
            f"but got '{actual_text}'"
        )
