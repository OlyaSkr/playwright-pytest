"""
    Page object for the Payment Page.
"""
import allure
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ProductsPage(BasePage):
    """
    Provides methods to interact with payment form fields,
    submit payment, and verify order placement.
    """
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
        self.page = page
        self.all_products_text = page.locator('h2.title.text-center')
        self.products_list = page.locator('div.features_items div.col-sm-4')
        self.first_product_view_button = self.products_list.first.locator(
            'a:has-text("View Product")')
        self.product_name = page.locator('div.product-information h2')
        self.category = page.locator(
            'div.product-information p:has-text("Category")')
        self.price = page.locator('div.product-information span span')
        self.availability = page.locator(
            'div.product-information p:has-text("Availability")')
        self.condition = page.locator(
            'div.product-information p:has-text("Condition")')
        self.brand = page.locator(
            'div.product-information p:has-text("Brand")')
        self.first_product_add_to_cart = self.products_list.first.locator(
            'a.btn.btn-default.add-to-cart').nth(1)
        self.cart_modal_continue_button = page.locator(
            'button:has-text("Continue Shopping")')
        self.second_product_add_to_cart = self.products_list.nth(1).locator(
            'a.btn.btn-default.add-to-cart').nth(1)
        self.view_cart_link = page.locator("a:has-text('View Cart')")
        self.sidebar_selector = page.locator("div.left-sidebar")
        self.brands_section = page.locator("div.brands_products")

    @allure.step("Verify 'All Products' text is visible")
    def verify_all_products_text(self, expected_text):
        """
        Verify All Products text is visible.
        """
        self.all_products_text.wait_for(state="visible", timeout=10000)
        actual_text = self.all_products_text.text_content()
        assert actual_text.strip() == expected_text, (
           f"Expected '{expected_text}' "
           f"but got '{actual_text}'"
        )

    @allure.step("Verify that products list is visible")
    def verify_products_list_visible(self):
        """
        Verifyproducts list is visible.
        """
        count = self.products_list.count()
        assert count > 0, "Products list is empty!"

        for i in range(count):
            self.products_list.nth(i).wait_for(state="visible", timeout=5000)

    @allure.step("Click on 'View Product' of the first product")
    def click_first_product_view(self):
        """
        Click on the View product buttonn for first product.
        """
        self.first_product_view_button.wait_for(state="visible", timeout=5000)
        self.first_product_view_button.click()

    @allure.step("Verify product details are visible")
    def verify_product_details_visible(self):
        """
        Verify product details are visible.
        """
        for locator, name in [
            (self.product_name, "Product Name"),
            (self.category, "Category"),
            (self.price, "Price"),
            (self.availability, "Availability"),
            (self.condition, "Condition"),
            (self.brand, "Brand"),
        ]:
            locator.wait_for(state="visible", timeout=5000)
            text = locator.text_content().strip()
            assert text != "", f"{name} is not visible or empty"

    @allure.step("Hover over and click on 'Add to Cart' of the first product")
    def add_first_product_to_cart(self):
        """
        Add first prodcut to cart.
        """
        self.products_list.first.wait_for(state="visible", timeout=5000)
        self.products_list.first.hover()
        self.first_product_add_to_cart.click()

    @allure.step("Click on 'Continue Shopping' button in cart modal")
    def click_continue_shopping_button(self):
        """
        Click Continue shopping button.
        """
        self.cart_modal_continue_button.wait_for(state="visible", timeout=5000)
        self.cart_modal_continue_button.click()

    @allure.step("Hover over and click on 'Add to Cart' of the second product")
    def add_second_product_to_cart(self):
        """
        Add second product to cart.
        """
        self.products_list.nth(1).wait_for(state="visible", timeout=5000)
        self.products_list.nth(1).hover()
        self.second_product_add_to_cart.click()

    @allure.step("Click on 'View Cart' button in cart modal")
    def click_view_cart_button(self):
        """
        Click View cart button.
        """
        self.view_cart_link.wait_for(state="visible", timeout=5000)
        self.view_cart_link.click()

    @allure.step("Verify category are visible")
    def verify_categories_visible(
        self,
        expected_header: str,
        expected_categories: list[str]
    ):
        """
        Verify category are visible.
        """
        expect(
           self.page.locator("div.left-sidebar h2").nth(0)
        ).to_have_text(expected_header)

        categories = self.page.locator("div.left-sidebar .panel-title a")
        expect(categories).to_have_count(len(expected_categories))
        for i, category_name in enumerate(expected_categories):
            expect(categories.nth(i)).to_have_text(category_name)

    @allure.step("Click on the category: {category_name}")
    def click_category(self, category_name: str):
        """
        Click on the category.
        """
        category_locator = self.sidebar_selector.locator(
            ".panel-title a", has_text=category_name
        )
        category_locator.wait_for(state="visible")
        category_locator.click()

    @allure.step(
        "Click on subcategory: {subcategory_name} "
        "under main category: {main_category}"
    )
    def click_subcategory(self, main_category: str, subcategory_name: str):
        """
        Click on the subcategory.
        """
        main_category_locator = self.sidebar_selector.locator(
            "h4.panel-title a", has_text=main_category
        )

        panel = self.page.locator(f"#{main_category}")
        panel_classes = panel.get_attribute("class") or ""
        if "collapse" in panel_classes:
            main_category_locator.click()

        subcategory_locator = panel.locator(
            ".panel-body ul li a",
            has_text=subcategory_name
        )

        subcategory_locator.wait_for(state="visible")
        subcategory_locator.click()

    @allure.step("Verify category page header contains: {expected_text}")
    def verify_category_page_header(self, expected_text: str):
        """
        Verify category page header.
        """
        header_locator = self.page.locator("h2.title")
        expect(header_locator).to_contain_text(expected_text, timeout=5000)

    @allure.step("Verify brands are visible on left sidebar")
    def verify_brands_visible(self, expected_brands: list[str]):
        """
        Verify that all brands in the left sidebar are visible.
        """
        expect(self.brands_section).to_be_visible()

        brand_links = self.brands_section.locator("ul.nav li a")
        expect(brand_links).to_have_count(len(expected_brands))

        for i, brand_name in enumerate(expected_brands):
            expect(brand_links.nth(i)).to_contain_text(brand_name)

    @allure.step("Click on brand: {brand_name}")
    def click_brand(self, brand_name: str):
        """
        Click on the brand.
        """
        brand_locator = self.brands_section.locator(
           f"ul.nav li a:has-text('{brand_name}')"
        )
        brand_locator.wait_for(state="visible")
        brand_locator.click()

    @allure.step("Verify brand page header contains: {expected_text}")
    def verify_brand_page_header(self, expected_text: str):
        """
        Verify brand page container.
        """
        header_locator = self.page.locator("h2.title")
        expect(header_locator).to_contain_text(expected_text, timeout=5000)
