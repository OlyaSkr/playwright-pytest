"""
This module contains a test for the Contact Us form functionality
on automationexercise.com using Playwright and Faker.
"""
from faker import Faker
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
from test_data.endpoints_data import endpoints

fake = Faker()


def test_contact_us_form(page, base_url):
    """
    Test the Contact Us form functionality on automationexercise.com.
    """
    home = HomePage(page, base_url)
    contact = ContactUsPage(page, base_url)

    home.goto("/")
    home.go_to_contact_us_form()
    expected_text = 'Get In Touch'
    contact.verify_get_in_touch_text(expected_text)

    random_name = fake.name()
    random_email = fake.email()
    random_subject = fake.sentence(nb_words=4)
    random_message = fake.paragraph(nb_sentences=3)

    contact.fill_contact_us_form(
        name=random_name,
        email=random_email,
        subject=random_subject,
        message=random_message
    )

    contact.click_submit_button()

    contact.verify_form_after_submit()
    assert page.url.endswith(endpoints["contact_us"])
