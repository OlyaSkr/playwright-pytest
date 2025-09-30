"""
    Test the newsletter subscription.
"""
import time
from faker import Faker
from pages.home_page import HomePage
from test_data.home_data import SUBSCRIPTION_TITLE

fake = Faker()


def generate_random_email():
    """
    Generate a random email using a fake first name and the current timestamp.
    """
    timestamp = int(time.time())
    return f"{fake.first_name().lower()}.{timestamp}@example.com"


def test_subscription_from_home_page(page, base_url):
    """
    Test the newsletter subscription form from the home page.
    """
    home = HomePage(page, base_url)
    random_email = generate_random_email()

    home.goto("/")
    home.scroll_to_footer()
    home.verify_subscription_text(SUBSCRIPTION_TITLE)
    home.fill_subscription_form(random_email)
    home.click_subscribe_button()
    home.verify_success_message("You have been successfully subscribed!")


def test_subscription_from_cart_page(page, base_url):
    """
    Test the newsletter subscription form from the cart page.
    """
    home = HomePage(page, base_url)
    random_email = generate_random_email()

    home.goto("/")
    home.go_to_cart_page()
    home.scroll_to_footer()
    home.verify_subscription_text(SUBSCRIPTION_TITLE)
    home.fill_subscription_form(random_email)
    home.click_subscribe_button()
    home.verify_success_message("You have been successfully subscribed!")
