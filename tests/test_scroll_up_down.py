"""
    Test Scroll Up using 'Arrow' button and without 'Arrow' button and
    Scroll Down functionality.
"""
from pages.home_page import HomePage
from test_data.home_data import SUBSCRIPTION_TITLE, HEADER_CAROUSEL_TEXT


def test_scroll_up_using_arrow_button(page, base_url):
    """
    Test Scroll Up using 'Arrow' button and
    Scroll Down functionality.
    """
    home = HomePage(page, base_url)

    home.goto("/")
    home.scroll_to_footer()
    home.verify_subscription_text(SUBSCRIPTION_TITLE)

    home.click_scroll_up_arrow_button()
    home.verify_header_carousel_texts(HEADER_CAROUSEL_TEXT)


def test_scroll_up_without_arrow_button(page, base_url):
    """
    Test Scroll Up without 'Arrow' button and
    Scroll Down functionality.
    """
    home = HomePage(page, base_url)

    home.goto("/")
    home.scroll_to_footer()
    home.verify_subscription_text(SUBSCRIPTION_TITLE)

    home.scroll_to_top_with_keyboard()
    home.verify_header_carousel_texts(HEADER_CAROUSEL_TEXT)
