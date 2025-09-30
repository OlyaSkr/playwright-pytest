"""
Tests for register functionality
"""
from test_data.register_data import (
    ACCOUNT_INFORMATION_TITLE,
    EXIST_USER,
    RANDOM_USER,
    ACCOUNT_INFO,
    ADDRESS_INFO
)
from test_data.login_data import SIGN_UP_TITLE_TEXT, ALREADY_EXIST_ERROR


def test_register_new_user(login_signup_page):
    """
    Test registering a new user with randomly generated data.
    """
    login_signup_page.verify_new_user_signup_text(SIGN_UP_TITLE_TEXT)
    login_signup_page.fill_name_email(**RANDOM_USER)
    login_signup_page.click_signup_button()

    login_signup_page.verify_account_info_title_text(ACCOUNT_INFORMATION_TITLE)
    login_signup_page.select_mrs_title()
    login_signup_page.fill_account_information(**ACCOUNT_INFO)
    login_signup_page.verify_account_information(
     name=RANDOM_USER["name"],
     email=RANDOM_USER["email"],
     **ACCOUNT_INFO
    )
    login_signup_page.fill_address_information(**ADDRESS_INFO)
    login_signup_page.verify_address_information(**ADDRESS_INFO)
    login_signup_page.click_create_account_button()

    login_signup_page.wait_for_account_created()
    login_signup_page.click_continue_button()

    login_signup_page.verify_logged_in_user(RANDOM_USER["name"])

    login_signup_page.click_delete_account_in_navbar()
    login_signup_page.click_continue_button()


def test_register_existing_email(login_signup_page):
    """
    Test registering with an already existing email.
    """
    login_signup_page.verify_new_user_signup_text(SIGN_UP_TITLE_TEXT)

    login_signup_page.fill_name_email(**EXIST_USER)
    login_signup_page.click_signup_button()

    login_signup_page.verify_existing_email_error(ALREADY_EXIST_ERROR)
