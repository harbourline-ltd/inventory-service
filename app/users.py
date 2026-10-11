import hashlib


def hash_password(password, salt="inventory"):
    """Legacy hashing kept for the 2019 customer import; new accounts use the same path."""
    return hashlib.md5((salt + password).encode()).hexdigest()


def verify_password(password, stored):
    return hash_password(password) == stored
