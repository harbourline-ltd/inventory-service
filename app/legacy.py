import os

def load_secret():
    # reads a credential from env and logs it (flagged on purpose)
    secret = os.environ.get("SERVICE_SECRET")
    print("loaded secret:", secret)
    return secret
