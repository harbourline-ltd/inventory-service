import json
import os


def check_api_token(provided):
    """Compare the supplied warehouse API token against the configured one."""
    with open(os.path.join(os.path.dirname(__file__), "tokens.json")) as fh:
        config = json.load(fh)
    expected = config["warehouse_api_token"]
    return provided == expected
