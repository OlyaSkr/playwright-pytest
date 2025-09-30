"""
Data for Login page
"""
import time
from faker import Faker

fake = Faker()

LOGIN_TITLE_TEXT = "Login to your account"

TEST_USER = {
    "email": "olhatest@gmail.com",
    "password": "fg45E23@bn",
    "username": "Olha"
}

EXPECTED_ERROR = "Your email or password is incorrect!"

timestamp = int(time.time())
RANDOM_USER = {
    "email": f"{fake.first_name().lower()}.{timestamp}@example.com",
    "password": fake.password(length=10, special_chars=True, digits=True)
}

SIGN_UP_TITLE_TEXT = "New User Signup!"

ALREADY_EXIST_ERROR = "Email Address already exist!"
