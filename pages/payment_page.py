"""
    Page object for the Payment Page.
"""
import os
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class PaymentPage(BasePage):
    """
    Provides methods to interact with payment form fields,
    submit payment, and verify order placement.
    """

    def __init__(self, page: Page, base_url: str):
        """
        Initialize PaymentPage with Playwright page and base URL.

        Args:
            page (Page): Playwright page object.
            base_url (str): Base URL of the application.
        """
        super().__init__(page, base_url)
        self.page = page
        self.name_on_card_input_field = self.page.locator(
            '[data-qa="name-on-card"]')
        self.card_number_input_field = self.page.locator(
            '[data-qa="card-number"]')
        self.cvc_input_field = self.page.locator('[data-qa="cvc"]')
        self.expiration_input_field = self.page.locator(
          '[data-qa="expiry-month"]')
        self.year_input_field = self.page.locator('[data-qa="expiry-year"]')
        self.pay_button = self.page.locator('button.submit-button')
        self.order_plasced_text = self.page.locator('[data-qa="order-placed"]')
        self.download_invoice_button = self.page.locator(
            'a:has-text("Download Invoice")'
            )

    @allure.step("Fill payment information")
    def fill_payment(self, name: str, card_number: str, cvc: str,
                     expiration: str, year: str):
        """
        Fill all payment fields in the payment form.
        """
        self.name_on_card_input_field.wait_for(state="visible", timeout=5000)
        self.name_on_card_input_field.fill(name)

        self.card_number_input_field.wait_for(state="visible", timeout=5000)
        self.card_number_input_field.fill(card_number)

        self.cvc_input_field.wait_for(state="visible", timeout=5000)
        self.cvc_input_field.fill(cvc)

        self.expiration_input_field.wait_for(state="visible", timeout=5000)
        self.expiration_input_field.fill(expiration)

        self.year_input_field.wait_for(state="visible", timeout=5000)
        self.year_input_field.fill(year)

    @allure.step("Click on 'Pay' button")
    def click_pay_button(self):
        """
        Click the 'Pay' button to submit the payment.

        Waits until the button is visible before clicking.
        """
        self.pay_button.wait_for(state="visible", timeout=5000)
        self.pay_button.click()

    @allure.step("Verify order placed message text")
    def verify_order_placed_text(self, expected_text: str):
        """
        Verify that the order placed confirmation text is visible and correct.
        """
        expect(self.order_plasced_text).to_be_visible(timeout=10000)
        actual_text = self.order_plasced_text.inner_text().strip()
        assert expected_text in actual_text, (
           f"Expected text '{expected_text}', "
           f"but got '{actual_text}'"
        )

    @allure.step("Download invoice")
    def download_invoice(self, save_path: str = "invoice.txt"):
        """
        Click on the Download Invoice button, save the file,
        and verify that it exists and is not empty.
        """
        self.download_invoice_button.wait_for(state="visible", timeout=5000)

        with self.page.expect_download() as download_info:
            self.download_invoice_button.click()

        download = download_info.value
        download.save_as(save_path)

        assert os.path.exists(save_path), (
            f"File '{save_path}' was not downloaded"
        )
        assert os.path.getsize(save_path) > 0, f"File '{save_path}' is empty"
