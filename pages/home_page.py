"""
    Page object for the Home Page.
"""
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.page = page
        self.base_url = base_url

        self.signup_login_btn = self.page.locator('a[href="/login"]')
        self.logged_in_user = self.page.locator('a:has-text("Logged in as")')
        self.home_slider = self.page.locator('div.carousel-inner')
        self.contact_us_link = self.page.locator('a:has-text("Contact us")')
        self.test_cases_link = self.page.get_by_role(
            "link", name="Test Cases", exact=True)
        self.products_link = self.page.locator(
            'a[href="/products"]', has_text="Products")
        self.cart_link = self.page.locator("ul.nav li a[href='/view_cart']")

        self.footer = self.page.locator('#footer')
        self.subscription_text = self.page.locator('div.single-widget h2')
        self.subscription_email_input_field = self.page.locator(
            '#susbscribe_email')
        self.subscribe_button = self.page.locator('#subscribe')
        self.success_subscription_message = self.page.locator(
            'div.alert-success.alert')
        self.recommended_items_title = self.page.locator(
            'div.recommended_items h2.title.text-center'
            )
        self.add_to_cart_buttons_in_recommended = self.page.locator(
            'div.carousel-inner .btn.btn-default.add-to-cart'
            )
        self.scroll_up_arrow_button = self.page.locator('a#scrollUp')
        self.header_carousel_text = self.page.locator('div#slider-carousel h2')

    @allure.step("Go to Home Page")
    def go_to_home(self):
        """
        Navigate to the Home page and wait until the home slider is visible.
        """
        self.goto("/")
        self.home_slider.wait_for(state="visible")

    @allure.step("Click on Signup / Login button")
    def go_to_signup_or_login(self):
        """
        Navigate to the Sign up/Login forms.
        """
        self.signup_login_btn.click()

    @allure.step("Verify user logged in as {username}")
    def verify_logged_in_user(self, username: str):
        """
        Verify that the logged-in user text contains the given username.
        """
        text = self.logged_in_user.inner_text().strip()
        assert username in text, (
          f"Expected username '{username}' "
          f"to appear in '{text}'"
        )

    @allure.step("Click on Contact us link in the header")
    def go_to_contact_us_form(self):
        """
        Navigate to the Contact us form.
        """
        self.contact_us_link.click()

    @allure.step("Click on Test Cases link in the header")
    def go_to_test_cases_page(self):
        """
        Navigate to the Test cases page.
        """
        self.test_cases_link.wait_for(state="visible")
        self.test_cases_link.click()

    @allure.step("Click on Products link in the header")
    def go_to_products_page(self):
        """
        Navigate to the Products page.
        """
        self.products_link.wait_for(state="visible")
        self.products_link.click()

    @allure.step("Click on Cart link in the header")
    def go_to_cart_page(self):
        """
        Navigate to the Cart page.
        """
        self.cart_link.wait_for(state="visible", timeout=10000)
        self.cart_link.click()

    @allure.step("Scroll down to footer")
    def scroll_to_footer(self):
        """
        Scroll to the footer.
        """
        self.footer.wait_for(state="visible")
        self.footer.scroll_into_view_if_needed()

    @allure.step("Verify 'Subscription' text is visible")
    def verify_subscription_text(self, expected_text: str):
        """
        Verify 'Subscription' text is visible.
        """
        self.subscription_text.wait_for(state="visible", timeout=10000)
        actual_text = self.subscription_text.text_content().strip()
        assert actual_text == expected_text, (
          f"Expected '{expected_text}' "
          f"but got '{actual_text}'"
        )

    @allure.step("Fill subscription form: email: {email}")
    def fill_subscription_form(self, email: str):
        """
        Fill subscription form.
        """
        self.subscription_email_input_field.wait_for(
         state="visible",
         timeout=10000
        )

        self.subscription_email_input_field.fill(email)

    @allure.step("Click on subscribe button")
    def click_subscribe_button(self):
        """
        Click on subscribe button after the button becomes visible.
        """
        self.subscribe_button.wait_for(state="visible")
        self.subscribe_button.click()

    @allure.step("Verify success message after subscription")
    def verify_success_message(self, expected_message: str):
        """
        Verify success message text after subscription.
        """
        self.success_subscription_message.wait_for(
            state="visible", timeout=5000
            )
        actual = self.success_subscription_message.text_content().strip()
        assert expected_message in actual, (
          f"Expected '{expected_message}', "
          f"but got '{actual}'"
        )

    @allure.step("Verify Recommended items titles")
    def verify_recommended_items_text(self, expected_text: str):
        """
        Verify Recommended items titles text.
        """
        recommended_items_title = self.recommended_items_title
        self.recommended_items_title.wait_for(
            state="visible",
            timeout=5000
        )
        expect(recommended_items_title).to_contain_text(expected_text)

    @allure.step(
        "Click on the first 'Add to cart' button "
        "in the Recommended items"
    )
    def click_first_add_to_cart(self):
        """
        Click on the first 'Add to cart' button in the Recommended items list.
        """
        first_add_to_cart = self.add_to_cart_buttons_in_recommended.first
        first_add_to_cart.wait_for(state="visible", timeout=40000)
        first_add_to_cart.click()

    @allure.step("Click on scroll up arrow button")
    def click_scroll_up_arrow_button(self):
        """
        Click on the croll up arrow button.
        """
        self.scroll_up_arrow_button.wait_for(state="visible")
        self.scroll_up_arrow_button.click()

    @allure.step("Verify all header carousel texts are the same")
    def verify_header_carousel_texts(self, expected_text: str):
        """
        Verify all header carousel elements display the same text.
        """
        elements = self.header_carousel_text
        count = elements.count()

        assert count > 0, "No header carousel text elements found"

        for i in range(count):
            elements.nth(i).wait_for(state="visible", timeout=20000)
            actual_text = elements.nth(i).text_content().strip()
            assert actual_text == expected_text, (
                f"Element {i}: expected '{expected_text}' "
                f"but got '{actual_text}'"
            )

    @allure.step("Scroll page to the top with keyboard")
    def scroll_to_top_with_keyboard(self):
        """
        Scroll the page to the top by pressing the Home key.
        """
        self.page.keyboard.press("Home")
