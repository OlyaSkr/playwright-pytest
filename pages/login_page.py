"""
    Page object for the Login Page.
"""
import allure
from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page, base_url: str):
        """
        Provides methods to interact with login form fields,
        submit form.
        """
        super().__init__(page, base_url)
        self.page = page
        self.base_url = base_url

        self.new_user_signup_text = self.page.locator("div.signup-form h2")
        self.name_input_field = self.page.locator('[data-qa="signup-name"]')
        self.sign_up_email_input_field = self.page.locator(
            '[data-qa="signup-email"]'
        )
        self.sign_up_button = self.page.locator('[data-qa="signup-button"]')
        self.mrs_title_radio = self.page.locator('#id_gender2')

        self.account_info_title = self.page.locator("h2.title").nth(0)
        self.name_field = self.page.locator("#name")
        self.email_field = self.page.locator("#email")
        self.password_field = self.page.locator('input[name="password"]')
        self.day_dropdown = self.page.locator('select[name="days"]')
        self.month_dropdown = self.page.locator('select[name="months"]')
        self.year_dropdown = self.page.locator('select[name="years"]')
        self.newsletter_checkbox = self.page.locator("#newsletter")
        self.special_offer_checkbox = self.page.locator("#optin")

        self.first_name = self.page.locator('#first_name')
        self.last_name = self.page.locator('#last_name')
        self.company = self.page.locator('#company')
        self.address_first = self.page.locator('#address1')
        self.address_second = self.page.locator('#address2')
        self.country = self.page.locator('#country')
        self.state = self.page.locator('#state')
        self.city = self.page.locator('#city')
        self.zipcode = self.page.locator("#zipcode")
        self.mobile_number = self.page.locator('#mobile_number')

        self.create_account_button = self.page.locator(
            '[data-qa="create-account"]'
            )
        self.account_created_text = self.page.locator(
            '[data-qa="account-created"]'
            )
        self.continue_button = self.page.locator('[data-qa="continue-button"]')
        self.logged_in_user_navbar_item = self.page.locator(
            "ul.nav li a:has-text('Logged in as')"
            )
        self.delete_account_navbar_item = self.page.locator(
            "ul.nav li a:has-text('Delete Account')"
            )

        self.verify_login_to_account_text = self.page.locator(
            'div.login-form h2'
            )
        self.login_email_input_field = self.page.locator(
            '[data-qa="login-email"]'
            )
        self.login_password_input_field = self.page.locator(
            '[data-qa="login-password"]'
            )
        self.login_button = self.page.locator('[data-qa="login-button"]')
        self.logout_navbar_item = self.page.locator(
            "ul.nav li a:has-text('Logout')"
            )

        self.name_on_card_input_field = self.page.locator(
            '[data-qa="name-on-card"]'
            )

    @allure.step("Verify 'New User Signup!' text is visible")
    def verify_new_user_signup_text(self, expected_text):
        """
        Verify 'New User Signup!' text is visible.
        """
        actual_text = self.new_user_signup_text.inner_text().strip()
        assert actual_text == expected_text, (
          f"Expected '{expected_text}' "
          f"but got '{actual_text}'"
        )

    @allure.step("Fill signup name: {name} and email: {email}")
    def fill_name_email(self, name, email):
        """
        Fill signup form.
        """
        self.name_input_field.fill(name)
        self.sign_up_email_input_field.fill(email)

    @allure.step("Click Signup button")
    def click_signup_button(self):
        """
        Click Signup button.
        """
        self.click(self.sign_up_button)

    @allure.step("Verify account information title text")
    def verify_account_info_title_text(self, expected_text):
        """
        Verify account information title.
        """
        self.account_info_title.wait_for(state="visible")
        actual_text = self.account_info_title.inner_text().strip()
        selector_info = getattr(
           self.account_info_title,
           "_selector",
           "<unknown selector>"
        )

        assert actual_text == expected_text, (
            f"Expected '{expected_text}' but got '{actual_text}' "
            f"for locator '{selector_info}'"
        )

    @allure.step("Select title 'Mrs.'")
    def select_mrs_title(self):
        """
        Select title 'Mrs.'
        """
        self.click(self.mrs_title_radio)

    @allure.step("Fill account information")
    def fill_account_information(
        self,
        password,
        day,
        month,
        year,
        newsletter=True,
        special_offer=True
     ):
        """
        Fill account information.
        """
        self.fill(self.password_field, password)
        self.select_option(self.day_dropdown, str(day))
        self.select_option(self.month_dropdown, str(month))
        self.select_option(self.year_dropdown, str(year))

        if newsletter:
            self.check(self.newsletter_checkbox)
        if special_offer:
            self.check(self.special_offer_checkbox)

    @allure.step("Verify account information is filled correctly")
    def verify_account_information(
        self,
        name,
        email,
        password,
        day,
        month,
        year,
        newsletter=True,
        special_offer=True
    ):
        """
        Verify account information is filled correctly.
        """
        assert self.get_value(self.name_field) == name, (
          f"Expected name '{name}' "
          f"but got '{self.get_value(self.name_field)}'"
        )
        assert self.get_value(self.email_field) == email, (
          f"Expected email '{email}' "
          f"but got '{self.get_value(self.email_field)}'"
        )
        assert self.get_value(self.password_field) != "", (
          "Password field is empty"
        )
        assert self.get_value(self.day_dropdown) == str(day)
        assert self.get_value(self.month_dropdown) == str(month)
        assert self.get_value(self.year_dropdown) == str(year)
        assert self.is_checked(self.newsletter_checkbox) == newsletter
        assert self.is_checked(self.special_offer_checkbox) == special_offer

    @allure.step("Fill address information")
    def fill_address_information(
        self,
        first_name,
        last_name,
        company,
        address1,
        address2,
        country,
        state,
        city,
        zipcode,
        mobile_number
    ):
        """
        Fill address information.
        """
        self.fill(self.first_name, first_name)
        self.fill(self.last_name, last_name)
        self.fill(self.company, company)
        self.fill(self.address_first, address1)
        self.fill(self.address_second, address2)
        self.select_option(self.country, country)
        self.fill(self.state, state)
        self.fill(self.city, city)
        self.fill(self.zipcode, zipcode)
        self.fill(self.mobile_number, mobile_number)

    @allure.step("Verify address information")
    def verify_address_information(
        self,
        first_name,
        last_name,
        company,
        address1,
        address2,
        country,
        state,
        city,
        zipcode,
        mobile_number
    ):
        """
        Verify address information.
        """
        assert self.get_value(self.first_name) == first_name
        assert self.get_value(self.last_name) == last_name
        assert self.get_value(self.company) == company
        assert self.get_value(self.address_first) == address1
        assert self.get_value(self.address_second) == address2
        assert self.get_value(self.country) == country
        assert self.get_value(self.state) == state
        assert self.get_value(self.city) == city
        assert self.get_value(self.zipcode) == zipcode
        assert self.get_value(self.mobile_number) == mobile_number

    @allure.step("Click Create Account button")
    def click_create_account_button(self):
        """
        Click Create Account button.
        """
        self.click(self.create_account_button)

    @allure.step("Wait for Account Created text to be visible")
    def wait_for_account_created(self, timeout=10000):
        """
        Wait for Account Created text to be visible.
        """
        self.account_created_text.wait_for(state="visible", timeout=timeout)

    @allure.step("Click Continue button")
    def click_continue_button(self):
        """
        Click Continue button.
        """
        self.click(self.continue_button)

    @allure.step("Verify user logged in as {username}")
    def verify_logged_in_user(self, username: str):
        """
        Verify user logged in.
        """
        text = self.get_text(self.logged_in_user_navbar_item)
        assert username in text, f"Expected username '{username}' in '{text}'"

    @allure.step("Click on Delete Account in the navbar")
    def click_delete_account_in_navbar(self):
        """
        Click on Delete Account in the navbar.
        """
        self.click(self.delete_account_navbar_item)

    @allure.step("Verify existing email error in the Sign up form")
    def verify_existing_email_error(self, expected_text):
        """
        Verify existing email error in the Sign up form.
        """
        error_message = self.page.locator("p", has_text=expected_text)
        error_message.wait_for(state="visible", timeout=5000)
        assert error_message.is_visible(), (
          f"Expected error message '{expected_text}' not visible"
        )

    @allure.step("Verify 'Login to your account' text is visible")
    def verify_login_to_your_account_text(self, expected_text: str):
        """
        Verify 'Login to your account' text is visible.
        """
        locator = self.verify_login_to_account_text
        locator.wait_for(state="visible", timeout=5000)
        actual_text = locator.text_content().strip()
        selector_info = getattr(locator, "_selector", "<unknown selector>")
        assert actual_text == expected_text, (
            f"Expected '{expected_text}' but got '{actual_text}' "
            f"for locator '{selector_info}'"
        )

    @allure.step("Fill login form: email: {email} and password: {password}")
    def fill_login_form(self, email, password):
        """
        Fill login form.
        """
        self.fill(self.login_email_input_field, email)
        self.fill(self.login_password_input_field, password)

    @allure.step("Click Login button")
    def click_login_button(self):
        """
        Click Login button.
        """
        self.click(self.login_button)

    @allure.step("Verify incorrect email or password error in the Login form")
    def verify_incorrect_email_or_password_error(self, expected_text):
        """
        Verify incorrect email or password error in the Login form.
        """
        error_message = self.page.locator(
           '[action="/login"] p',
           has_text=expected_text
        )

        error_message.wait_for(state="visible", timeout=5000)
        actual_text = error_message.text_content().strip()
        print(f"Error message displayed: {actual_text}")
        assert actual_text == expected_text, (
            f"Expected error message '{expected_text}' but got '{actual_text}'"
        )

    @allure.step("Click Logout button")
    def click_logout_button(self):
        """
        Click Logout button.
        """
        self.click(self.logout_navbar_item)
