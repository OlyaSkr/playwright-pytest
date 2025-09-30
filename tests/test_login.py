"""
Tests for login functionality on automationexercise.com.

Includes:
- Valid login
- Invalid login
- Logout
"""

from faker import Faker
from test_data.endpoints_data import endpoints
from test_data.login_data import (
    LOGIN_TITLE_TEXT,
    TEST_USER,
    EXPECTED_ERROR,
    RANDOM_USER
)


fake = Faker()


def test_login_with_valid_data(login_signup_page, login_user):
    """Test login with valid credentials."""
    login_signup_page.verify_login_to_your_account_text(LOGIN_TITLE_TEXT)
    login_user(**TEST_USER)


def test_login_with_incorrect_email_and_password(login_signup_page):
    """Test login with invalid credentials and verify error message."""
    login_signup_page.verify_login_to_your_account_text(LOGIN_TITLE_TEXT)

    login_signup_page.fill_login_form(**RANDOM_USER)
    login_signup_page.click_login_button()

    login_signup_page.verify_incorrect_email_or_password_error(EXPECTED_ERROR)


def test_logout(login_signup_page, login_user):
    """Test logging out after a successful login."""
    login_signup_page.verify_login_to_your_account_text(LOGIN_TITLE_TEXT)

    login_user(**TEST_USER)
    login_signup_page.click_logout_button()

    login_signup_page.page.wait_for_url(endpoints["login"])
    login_signup_page.verify_login_to_your_account_text(LOGIN_TITLE_TEXT)
