# Example of a custom module to be imported

import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email))