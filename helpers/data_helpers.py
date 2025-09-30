"""
Helper module to generate random user and payment data for testing.
"""
import random
import time
import string
from faker import Faker

fake = Faker()


def generate_password(length=10):
    """
    Generate a random password
    """
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_chars) for _ in range(length))


def generate_random_user():
    """
    Generate a random user with personal info, email, password, date of birth,
    and address details.
    """
    timestamp = int(time.time())
    first_name = fake.first_name()
    last_name = fake.last_name()
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": f"{first_name.lower()}.{timestamp}@example.com",
        "password": generate_password(10),
        "day": str(random.randint(1, 28)),
        "month": str(random.randint(1, 12)),
        "year": str(random.randint(1970, 2005)),
        "address": {
            "first_name": first_name,
            "last_name": last_name,
            "company": fake.company(),
            "address1": fake.street_address(),
            "address2": fake.secondary_address(),
            "country": "United States",
            "state": fake.state(),
            "city": fake.city(),
            "zipcode": fake.zipcode(),
            "mobile_number": fake.phone_number(),
        },
    }


def generate_random_payment():
    """
    Generate random payment card details for testing checkout/payment forms.
    """
    return {
        "name": fake.name(),
        "card_number": str(random.randint(4000000000000000, 4999999999999999)),
        "cvc": str(random.randint(100, 999)),
        "month": str(random.randint(1, 12)).zfill(2),
        "year": str(random.randint(2025, 2030)),
    }
