"""
    Page object for the Checkout Page.
"""
import re
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Checkout class representing page objects with actions."""
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.page = page
        self.delivery_address = page.locator("#address_delivery")
        self.billing_address = page.locator("#address_invoice")
        self.product_name = page.locator(".cart_description h4 a")
        self.category = page.locator(".cart_description p")
        self.price = page.locator(".cart_price p")
        self.quantity = page.locator(".cart_quantity button")
        self.total = page.locator(".cart_total p")
        self.comment_textarea = page.locator("textarea[name='message']")
        self.place_order_button = page.locator(
            'a[href="/payment"]', has_text="Place Order"
            )

    @allure.step("Verify delivery and billing addresses")
    def verify_addresses(
        self,
        expected_delivery_components: dict,
        expected_billing_components: dict
    ):
        """
        Verify delivery and billing addresses.
        """
        expect(self.delivery_address).to_be_visible()
        expect(self.billing_address).to_be_visible()

        delivery_text = re.sub(
            r"\s+",
            " ",
            self.delivery_address.inner_text()
        ).strip().lower()

        billing_text = re.sub(
            r"\s+",
            " ",
            self.billing_address.inner_text()
        ).strip().lower()

        for key, value in expected_delivery_components.items():
            assert str(value).lower() in delivery_text, (
                f"{key} '{value}' not found in delivery address: "
                f"'{delivery_text}'"
            )

        for key, value in expected_billing_components.items():
            assert str(value).lower() in billing_text, (
                f"{key} '{value}' not found in billing address: "
                f"'{billing_text}'"
            )

    @allure.step("Verify Review Your Order")
    def verify_product_details_visible(self):
        """
        Verify product details in the Review your order.
        """
        for locator, name in [
            (self.product_name, "Product Name"),
            (self.category, "Category"),
            (self.price, "Price"),
            (self.quantity, "Quantity"),
            (self.total, "Total"),
        ]:
            locator.wait_for(state="visible", timeout=5000)
            text = locator.text_content().strip()
            assert text != "", f"{name} is not visible or empty"

    @allure.step("Fill comment in the checkout: comment: {comment}")
    def fill_comment_input_field(self, comment):
        """
        Fill comment in the input field in the checkout.
        """
        self.comment_textarea.fill(comment)

    @allure.step("Click on 'Place Order' button")
    def click_place_order_button(self):
        """
        Click on 'Place Order' button
        """
        self.place_order_button.wait_for(state="visible", timeout=5000)
        self.place_order_button.click()
