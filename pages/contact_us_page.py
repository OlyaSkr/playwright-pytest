"""
    Page object for the Contact us Page.
"""
import logging
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class ContactUsPage(BasePage):
    """
    Provides methods to interact with Contact us form fields.
    """
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.page = page
        self.get_in_touch_text = self.page.locator('div.contact-form h2.title')
        self.name_input_field = self.page.locator('[data-qa="name"]')
        self.email_input_field = self.page.locator('[data-qa="email"]')
        self.subject_input_field = self.page.locator('[data-qa="subject"]')
        self.message_input_field = self.page.locator('[data-qa="message"]')
        self.upload_input = self.page.locator('input[name="upload_file"]')
        self.submit_button = self.page.locator(
            'input[data-qa="submit-button"]'
            )
        self.success_message = self.page.locator(
            'div.status.alert.alert-success'
            )
        self.home_link = self.page.locator('a.btn-success')

    @allure.step("Verify 'GET IN TOUCH' text is visible")
    def verify_get_in_touch_text(self, expected_text):
        """
        Verify 'GET IN TOUCH' text is visible.
        """
        self.get_in_touch_text.wait_for(state="visible", timeout=5000)
        actual_text = self.get_in_touch_text.text_content()
        assert actual_text.strip() == expected_text, (
          f"Expected '{expected_text}' "
          f"but got '{actual_text.strip()}'"
        )

    @allure.step("Fill Contact Us form")
    def fill_contact_us_form(
        self,
        name: str,
        email: str,
        subject: str,
        message: str
       ):
        """
        Fill Contact us input fields.
        """
        self.name_input_field.wait_for(state="visible", timeout=5000)
        self.name_input_field.fill(name)
        self.email_input_field.wait_for(state="visible", timeout=5000)
        self.email_input_field.fill(email)
        self.subject_input_field.wait_for(state="visible", timeout=5000)
        self.subject_input_field.fill(subject)
        self.message_input_field.wait_for(state="visible", timeout=5000)
        self.message_input_field.fill(message)

    @allure.step("Click Submit button")
    def click_submit_button(self):
        """
        Click on the Submit button.
        """
        self.submit_button.wait_for(state="attached", timeout=10000)
        self.submit_button.scroll_into_view_if_needed()
        self.submit_button.click(force=True)

    @allure.step("Verify form after submit")
    def verify_form_after_submit(self):
        """
        Verify form after submit.
        """
        self.name_input_field.wait_for(state="visible", timeout=10000)
        assert self.name_input_field.input_value() == ""
        assert self.email_input_field.input_value() == ""
        assert self.subject_input_field.input_value() == ""
        assert self.message_input_field.input_value() == ""
