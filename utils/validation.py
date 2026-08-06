import email


def is_valid_phone(phone: str):
    return phone.isdigit() and len(phone) == 10

def is_valid_email(email: str):
    return "@" in email and "." in email

def is_positive_price(price: int):
    return price > 0

def ís_positive_capacity(capacity: int):
    return capacity > 0
