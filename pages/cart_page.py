"""
    Page object for the Cart Page.
"""
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CartPage(BasePage):
    """Cart class representing page objects with actions."""
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.page = page
        self.product_rows = page.locator("table#cart_info_table tbody tr")
        self.quantity_button = page.locator("td.cart_quantity button")
        self.proceed_to_checkout_button = page.locator(
            'a.btn.btn-default.check_out'
            )
        self.register_login_link = page.locator(
            'a[href="/login"]', has_text="Register / Login"
            )

    @allure.step("Verify product in cart")
    def verify_product(
       self,
       product_id: str,
       expected_price: str,
       expected_qty: str,
       expected_total: str
    ):
        """
        Verify product details in cart
        """
        row = self.page.locator(f"tr#{product_id}")
        price = row.locator(".cart_price p")
        qty = row.locator(".cart_quantity button")
        total = row.locator(".cart_total p")

        expect(price).to_have_text(expected_price)
        expect(qty).to_have_text(expected_qty)
        expect(total).to_have_text(expected_total)

    @allure.step("Get number of products in cart")
    def get_product_count(self):
        """
        Get number of products in cart
        """
        return self.product_rows.count()

    @allure.step("Verify quantity of product is {expected_quantity}")
    def verify_quantity(self, expected_quantity: int):
        """
        Verify product quantity
        """
        quantity_text = self.quantity_button.inner_text()
        actual_quantity = int(quantity_text)
        assert actual_quantity == expected_quantity, (
         f"Expected quantity {expected_quantity}, "
         f"but got {actual_quantity}"
        )

    @allure.step("Click on 'Proceed to checkout' button in view cart page")
    def click_proceed_to_checkout_button(self):
        """
        Click on 'Proceed to checkout' button in view cart page
        """
        self.proceed_to_checkout_button.wait_for(state="visible", timeout=5000)
        self.proceed_to_checkout_button.click()

    @allure.step("Click on 'Register/Login' link in Checkout")
    def click_register_login_link(self):
        """
        Click on 'Register/Login' link in Checkout
        """
        self.register_login_link.wait_for(state="visible", timeout=5000)
        self.register_login_link.click()

    def delete_product_by_id(self, product_id: str):
        """
        Clicks the delete button for a specific product by data-product-id
        """
        selector = f"a.cart_quantity_delete[data-product-id='{product_id}']"
        self.page.click(selector)

    def delete_multiple_products(self, product_ids: list[str]):
        """
        Delete multiple products from the cart by their IDs
        """
        for product_id in product_ids:
            self.delete_product_by_id(product_id)
            selector = (
               f"a.cart_quantity_delete"
               f"[data-product-id='{product_id}']"
            )
            expect(self.page.locator(selector)).not_to_be_visible()

    def verify_product_removed(self, product_id: str):
        """
        Verify the product is no longer visible in the cart
        """
        selector = f"a.cart_quantity_delete[data-product-id='{product_id}']"
        expect(self.page.locator(selector)).not_to_be_visible()
