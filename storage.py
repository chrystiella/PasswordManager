import json
import os

PASSWORD_FILE = "passwords.txt"

def save_password(website, username, encrypted_password):
    """Saves a password entry to the storage file."""
    data = {}
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    data[website] = {"username": username, "password": encrypted_password}

    with open(PASSWORD_FILE, "w") as file:
        json.dump(data, file, indent=4)

def retrieve_password(website):
    """Retrieves an encrypted password for a given website."""
    if not os.path.exists(PASSWORD_FILE):
        return None, None

    with open(PASSWORD_FILE, "r") as file:
        try:
            data = json.load(file)
            if website in data:
                return data[website]["username"], data[website]["password"]
        except json.JSONDecodeError:
            return None, None

    return None, None
