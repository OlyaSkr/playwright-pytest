"""
This module contains a test for the Test Cases page.
"""
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.test_cases_page import CasesPage
from test_data.endpoints_data import endpoints


def test_cases_page(page, base_url):
    """
    Test navigation to the Test Cases page and verify the title and URL.
    """
    home = HomePage(page, base_url)
    cases = CasesPage(page, base_url)
    expected_title = "Automation Practice Website for UI Testing - Test Cases"

    home.goto("/")
    home.go_to_test_cases_page()

    cases.verify_test_cases_text('Test Cases')

    assert page.title() == expected_title, (
       f"Expected title: {expected_title}, "
       f"got: {page.title()}"
    )

    expect(page).to_have_url(endpoints["test_cases"])
