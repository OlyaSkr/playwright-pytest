"""
  Page object for the Product Detail Page.
"""
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ProductDetailPage(BasePage):
    """
    Provides methods to interact with the product detail page elements
    """
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.page = page
        self.quantity_input_field = page.locator('input#quantity')
        self.add_to_cart_button = page.locator('button.btn.btn-default.cart')
        self.active_tab = page.locator('li.active > a')
        self.your_name_input_field = page.locator('[id="name"]')
        self.email_address_input_field = page.locator('[id="email"]')
        self.review_input_field = page.locator('[id="review"]')
        self.review_button = page.locator('[id="button-review"]')
        self.success_review_send_message = page.locator(
            'div.alert-success.alert span'
            )

    @allure.step("Fill quantity input field: quantity: {quantity}")
    def fill_quantity_field(self, quantity):
        """
        Fill the quantity input field with the specified number.
        """
        self.quantity_input_field.wait_for(state="visible", timeout=5000)
        self.quantity_input_field.click()
        self.quantity_input_field.press("Control+A")
        self.quantity_input_field.press("Backspace")
        self.quantity_input_field.type(str(quantity))

    @allure.step("Click on 'Add to Cart' button")
    def click_continue_shopping_button(self):
        """
        Click the 'Add to Cart' button to add the selected product
        to the shopping cart.
        """
        self.add_to_cart_button.wait_for(state="visible", timeout=5000)
        self.add_to_cart_button.click()

    @allure.step("Verify active tab contains text: {expected_text}")
    def verify_active_tab_text(self, expected_text: str):
        """
        Verify that the currently active tab contains the expected text.
        """
        expect(self.active_tab).to_contain_text(expected_text)

    @allure.step("Fill review product form")
    def fill_review_product_form(self, name, email, review):
        """
        Fill the review product forn.
        """
        self.your_name_input_field.wait_for(state="visible", timeout=5000)
        self.your_name_input_field.fill(name)
        self.email_address_input_field.wait_for(state="visible", timeout=5000)
        self.email_address_input_field.fill(email)
        self.review_input_field.wait_for(state="visible", timeout=5000)
        self.review_input_field.fill(review)

    @allure.step("Click on Submit button")
    def click_submit_button(self):
        """
        Click the Submit button.
        """
        self.review_button.wait_for(state="visible", timeout=5000)
        self.review_button.click()

    @allure.step("Verify success message after submitting review")
    def verify_review_success_message(self, expected_text: str):
        """
        Verify that the success message is displayed with the expected text.
        """
        success_message = self.success_review_send_message
        self.success_review_send_message.wait_for(
            state="visible",
            timeout=5000
        )
        expect(success_message).to_contain_text(expected_text)
