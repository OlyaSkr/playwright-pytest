"""
    Test place order before register, after register a new user
    and after login.
    """
from playwright.sync_api import expect
from faker import Faker
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.payment_page import PaymentPage
from pages.checkout_page import CheckoutPage
from helpers.data_helpers import generate_random_user, generate_random_payment
from test_data.products_data import ALL_PRODUCTS_TITLE
from test_data.register_data import ACCOUNT_INFORMATION_TITLE
from test_data.login_data import SIGN_UP_TITLE_TEXT
from test_data.order_data import ORDER_PLACED_TITLE
from test_data.login_data import LOGIN_TITLE_TEXT
from test_data.endpoints_data import endpoints

fake = Faker()


def test_register_while_place_order(products_page, page, base_url):
    """
    Test register new user while place order.
    """
    products = products_page
    cart = CartPage(page, base_url)
    login = LoginPage(page, base_url)
    home = HomePage(page, base_url)
    checkout = CheckoutPage(page, base_url)
    payment = PaymentPage(page, base_url)
    user = generate_random_user()
    payment_data = generate_random_payment()

    products.verify_all_products_text(ALL_PRODUCTS_TITLE)
    products.verify_products_list_visible()
    expect(page).to_have_url(endpoints["products"])

    products.add_first_product_to_cart()
    products.click_view_cart_button()
    expect(page).to_have_url(endpoints["view_cart"])

    cart.click_proceed_to_checkout_button()
    cart.click_register_login_link()
    login.verify_new_user_signup_text(SIGN_UP_TITLE_TEXT)

    login.fill_name_email(user["first_name"], user["email"])
    login.click_signup_button()
    login.verify_account_info_title_text(ACCOUNT_INFORMATION_TITLE)
    login.select_mrs_title()
    login.fill_account_information(
        password=user["password"],
        day=user["day"],
        month=user["month"],
        year=user["year"],
        newsletter=True,
        special_offer=True,
    )
    login.fill_address_information(**user["address"])
    login.click_create_account_button()
    login.wait_for_account_created()
    login.click_continue_button()
    login.verify_logged_in_user(user["first_name"])

    home.go_to_cart_page()
    expect(page).to_have_url(endpoints["view_cart"])
    cart.click_proceed_to_checkout_button()

    checkout.verify_addresses(
        expected_delivery_components=user["address"],
        expected_billing_components=user["address"],
    )
    checkout.verify_product_details_visible()
    checkout.fill_comment_input_field(fake.text(max_nb_chars=200))
    checkout.click_place_order_button()

    payment.fill_payment(
        name=payment_data["name"],
        card_number=payment_data["card_number"],
        cvc=payment_data["cvc"],
        expiration=payment_data["month"],
        year=payment_data["year"],
    )
    payment.click_pay_button()
    payment.verify_order_placed_text(ORDER_PLACED_TITLE)

    login.click_delete_account_in_navbar()
    login.click_continue_button()


def test_register_before_place_order(page, base_url):
    """
    Test register new user before place order.
    """
    products = ProductsPage(page, base_url)
    cart = CartPage(page, base_url)
    login = LoginPage(page, base_url)
    home = HomePage(page, base_url)
    checkout = CheckoutPage(page, base_url)
    payment = PaymentPage(page, base_url)
    user = generate_random_user()
    payment_data = generate_random_payment()

    home.goto("/")
    home.go_to_signup_or_login()
    login.verify_new_user_signup_text(SIGN_UP_TITLE_TEXT)

    login.fill_name_email(user["first_name"], user["email"])
    login.click_signup_button()
    login.verify_account_info_title_text(ACCOUNT_INFORMATION_TITLE)
    login.select_mrs_title()
    login.fill_account_information(
        password=user["password"],
        day=user["day"],
        month=user["month"],
        year=user["year"],
        newsletter=True,
        special_offer=True,
    )
    login.fill_address_information(**user["address"])
    login.click_create_account_button()
    login.wait_for_account_created()
    login.click_continue_button()
    login.verify_logged_in_user(user["first_name"])

    home.go_to_products_page()
    products.verify_all_products_text(ALL_PRODUCTS_TITLE)
    products.verify_products_list_visible()
    expect(page).to_have_url(endpoints["products"])

    products.add_first_product_to_cart()
    products.click_view_cart_button()
    expect(page).to_have_url(endpoints["view_cart"])

    cart.click_proceed_to_checkout_button()

    checkout.verify_addresses(
        expected_delivery_components=user["address"],
        expected_billing_components=user["address"],
    )
    checkout.verify_product_details_visible()
    checkout.fill_comment_input_field(fake.text(max_nb_chars=200))
    checkout.click_place_order_button()

    payment.fill_payment(
        name=payment_data["name"],
        card_number=payment_data["card_number"],
        cvc=payment_data["cvc"],
        expiration=payment_data["month"],
        year=payment_data["year"],
    )
    payment.click_pay_button()
    payment.verify_order_placed_text(ORDER_PLACED_TITLE)

    login.click_delete_account_in_navbar()
    login.click_continue_button()


def test_login_before_place_order(page, base_url, login_user):
    """
    Test login before place order.
    """
    products = ProductsPage(page, base_url)
    cart = CartPage(page, base_url)
    login = LoginPage(page, base_url)
    home = HomePage(page, base_url)
    checkout = CheckoutPage(page, base_url)
    payment = PaymentPage(page, base_url)

    user = generate_random_user()
    payment_data = generate_random_payment()

    home.goto("/")
    home.go_to_signup_or_login()
    login.verify_new_user_signup_text(SIGN_UP_TITLE_TEXT)

    login.fill_name_email(user["first_name"], user["email"])
    login.click_signup_button()

    login.select_mrs_title()
    login.fill_account_information(
        password=user["password"],
        day=user["day"],
        month=user["month"],
        year=user["year"],
        newsletter=True,
        special_offer=True,
    )
    login.fill_address_information(**user["address"])
    login.click_create_account_button()
    login.wait_for_account_created()
    login.click_continue_button()
    login.verify_logged_in_user(user["first_name"])

    login.click_logout_button()
    login.page.wait_for_url(endpoints["login"])
    login.verify_login_to_your_account_text(LOGIN_TITLE_TEXT)

    login_user(user["email"], user["password"], user["first_name"])

    home.go_to_products_page()
    products.verify_all_products_text(ALL_PRODUCTS_TITLE)
    products.verify_products_list_visible()
    expect(page).to_have_url(endpoints["products"])

    products.add_first_product_to_cart()
    products.click_view_cart_button()
    expect(page).to_have_url(endpoints["view_cart"])

    cart.click_proceed_to_checkout_button()

    checkout.verify_addresses(
        expected_delivery_components=user["address"],
        expected_billing_components=user["address"],
    )
    checkout.verify_product_details_visible()
    checkout.fill_comment_input_field(fake.text(max_nb_chars=200))
    checkout.click_place_order_button()

    payment.fill_payment(
        name=payment_data["name"],
        card_number=payment_data["card_number"],
        cvc=payment_data["cvc"],
        expiration=payment_data["month"],
        year=payment_data["year"],
    )
    payment.click_pay_button()
    payment.verify_order_placed_text(ORDER_PLACED_TITLE)

    login.click_delete_account_in_navbar()
    login.click_continue_button()
