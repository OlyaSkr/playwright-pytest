"""
Data for Sign up page
"""

import random
import time
from faker import Faker

fake = Faker()

ACCOUNT_INFORMATION_TITLE = "ENTER ACCOUNT INFORMATION"

EXIST_USER = {
    "name": "test",
    "email": "test@gmail.com"
}

RANDOM_USER = {
    "name": fake.first_name(),
    "email": f"{fake.first_name().lower()}.{int(time.time())}@example.com"
}

ACCOUNT_INFO = {
    "password": fake.password(length=10, special_chars=True, digits=True),
    "day": str(random.randint(1, 28)),
    "month": str(random.randint(1, 12)),
    "year": str(random.randint(1970, 2005)),
    "newsletter": True,
    "special_offer": True
}

ADDRESS_INFO = {
    "first_name": RANDOM_USER["name"],
    "last_name": fake.last_name(),
    "company": fake.company(),
    "address1": fake.street_address(),
    "address2": fake.secondary_address(),
    "country": "United States",
    "state": fake.state(),
    "city": fake.city(),
    "zipcode": fake.zipcode(),
    "mobile_number": fake.phone_number()
}
