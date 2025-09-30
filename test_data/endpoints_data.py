"""
Data pages endpoints
"""
BASE_URL = "https://automationexercise.com"

endpoints = {
    "products": f"{BASE_URL}/products",
    "view_cart": f"{BASE_URL}/view_cart",
    "login": f"{BASE_URL}/login",
    "checkout": f"{BASE_URL}/checkout",
    "payment": f"{BASE_URL}/payment",
    "account_delete": f"{BASE_URL}/delete_account",
    "product_details": f"{BASE_URL}/product_details/{{id}}",
    "contact_us": f"{BASE_URL}/contact_us",
    "test_cases": f"{BASE_URL}/test_cases"
}
