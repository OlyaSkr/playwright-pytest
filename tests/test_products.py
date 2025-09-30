"""
    Test products, product detail and cart pages.
"""
from playwright.sync_api import expect
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from test_data.products_data import (
    products_in_cart,
    ALL_PRODUCTS_TITLE,
    QUANTITY_VALUE,
    CATEGORIES,
    WOMEN_DRESS_SUBCATEGORY,
    KIDS_TOP_SUBCATEGORY,
    BRANDS,
    POLO_BRAND_TITLE,
    HM_BRAND_TITLE,
    REVIEW_TITLE,
    RANDOM_USER,
    SUCCESS_MESSAGE
)
from test_data.home_data import RECOMMENDED_ITEMS_TITLE
from test_data.endpoints_data import endpoints


def test_all_products_and_product_detail_page(products_page, page, base_url):
    """
    Test all products are visible and product detail page is visible.
    """
    products = products_page

    products.verify_all_products_text(ALL_PRODUCTS_TITLE)
    expect(page).to_have_url(f"{base_url}/products")
    products.verify_products_list_visible()

    products.click_first_product_view()
    expect(page).to_have_url(f"{base_url}/product_details/1")
    products.verify_product_details_visible()


def test_add_products_to_cart(products_page, page, base_url):
    """
    Test add products to the cart.
    """
    products = products_page
    cart = CartPage(page, base_url)

    products.verify_all_products_text(ALL_PRODUCTS_TITLE)
    expect(page).to_have_url(endpoints["products"])
    products.verify_products_list_visible()

    products.add_first_product_to_cart()
    products.click_continue_shopping_button()
    products.add_second_product_to_cart()
    products.click_view_cart_button()

    expect(page).to_have_url(endpoints["view_cart"])
    for product in products_in_cart:
        cart.verify_product(
            product["name"],
            product["price"],
            product["quantity"],
            product["total"]
        )

    assert cart.get_product_count() == len(products_in_cart)


def test_products_quantity_in_cart(products_page, page, base_url):
    """
    Test product quantity in the cart.
    """
    products = products_page
    product_detail = ProductDetailPage(page, base_url)
    cart = CartPage(page, base_url)

    products.verify_all_products_text(ALL_PRODUCTS_TITLE)
    expect(page).to_have_url(endpoints["products"])
    products.verify_products_list_visible()

    products.click_first_product_view()
    expect(page).to_have_url(endpoints["product_details"].format(id=1))
    products.verify_product_details_visible()

    product_detail.fill_quantity_field(QUANTITY_VALUE)
    product_detail.click_continue_shopping_button()

    products.click_view_cart_button()

    expect(page).to_have_url(endpoints["view_cart"])
    cart.verify_quantity(QUANTITY_VALUE)


def test_remove_products_from_cart(products_page, page, base_url):
    """
    Test remove products from the cart.
    """
    products = products_page
    cart = CartPage(page, base_url)

    products.verify_all_products_text(ALL_PRODUCTS_TITLE)
    expect(page).to_have_url(f"{base_url}/products")
    products.verify_products_list_visible()

    products.add_first_product_to_cart()
    products.click_continue_shopping_button()
    products.add_second_product_to_cart()
    products.click_view_cart_button()

    expect(page).to_have_url(endpoints["view_cart"])

    product_ids = ["1", "2"]

    cart.delete_multiple_products(product_ids)

    for pid in product_ids:
        cart.verify_product_removed(pid)


def test_products_category(products_page):
    """
    Test products category.
    """
    products = products_page

    products.verify_categories_visible(
     expected_header=CATEGORIES["main"],
     expected_categories=list(CATEGORIES["sub"].keys())
    )

    products.click_category("Women")
    products.click_subcategory("Women", CATEGORIES["sub"]["Women"][0])
    products.verify_category_page_header(WOMEN_DRESS_SUBCATEGORY)

    products.click_category("Kids")
    products.click_subcategory("Kids", CATEGORIES["sub"]["Kids"][1])
    products.verify_category_page_header(KIDS_TOP_SUBCATEGORY)


def test_products_brand(products_page):
    """
    Test products brand.
    """
    products = products_page

    products.verify_brands_visible(BRANDS)

    products.click_brand(BRANDS[0])
    products.verify_brand_page_header(POLO_BRAND_TITLE)

    products.click_brand(BRANDS[1])
    products.verify_brand_page_header(HM_BRAND_TITLE)


def test_review_on_product(products_page, page, base_url):
    """
    Test review on product.
    """
    products = products_page
    product_detail = ProductDetailPage(page, base_url)

    products.verify_all_products_text(ALL_PRODUCTS_TITLE)
    expect(page).to_have_url(f"{base_url}/products")

    products.click_first_product_view()
    expect(page).to_have_url(f"{base_url}/product_details/1")
    products.verify_product_details_visible()

    product_detail.verify_active_tab_text(REVIEW_TITLE)
    product_detail.fill_review_product_form(**RANDOM_USER)
    product_detail.click_submit_button()

    product_detail.verify_review_success_message(SUCCESS_MESSAGE)


def test_add_product_from_recommended_list(page, base_url):
    """
    Test add product to the cart from the recommended list.
    """
    products = ProductsPage(page, base_url)
    cart = CartPage(page, base_url)
    home = HomePage(page, base_url)

    home.goto("/")
    home.scroll_to_footer()

    home.verify_recommended_items_text(RECOMMENDED_ITEMS_TITLE)
    home.click_first_add_to_cart()

    products.click_view_cart_button()
    expect(page).to_have_url(endpoints["view_cart"])

    first_product = products_in_cart[0]

    cart.verify_product(
        first_product["name"],
        first_product["price"],
        first_product["quantity"],
        first_product["total"]
    )

    assert cart.get_product_count() >= 1
