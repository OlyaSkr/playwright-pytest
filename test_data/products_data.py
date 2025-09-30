"""
Data for Products and Product detail pages.
"""

import time
from faker import Faker

fake = Faker()
products_in_cart = [
    {
        "name": "product-1",
        "price": "Rs. 500",
        "quantity": "1",
        "total": "Rs. 500"
    },
    {
        "name": "product-2",
        "price": "Rs. 400",
        "quantity": "1",
        "total": "Rs. 400"
    }
]

ALL_PRODUCTS_TITLE = "All Products"

QUANTITY_VALUE = 4

CATEGORIES = {
    "main": ["Category"],
    "sub": {
        "Women": ["Dress", "Tops", "Saree"],
        "Men": ["Tshirts", "Jeans"],
        "Kids": ["Dress", "Tops & Shirts"]
    }
}

WOMEN_DRESS_SUBCATEGORY = "Women - Dress Products"

KIDS_TOP_SUBCATEGORY = "Kids - Tops & Shirts Products"

BRANDS = [
    "Polo",
    "H&M",
    "Madame",
    "Mast & Harbour",
    "Babyhug",
    "Allen Solly Junior",
    "Kookie Kids",
    "Biba"
]

POLO_BRAND_TITLE = "Brand - Polo Products"

HM_BRAND_TITLE = "Brand - H&M Products"

REVIEW_TITLE = "Write Your Review"

RANDOM_USER = {
    "name": fake.first_name(),
    "email": f"{fake.first_name().lower()}.{int(time.time())}@example.com",
    "review": fake.text(max_nb_chars=100)
}

SUCCESS_MESSAGE = "Thank you for your review."
