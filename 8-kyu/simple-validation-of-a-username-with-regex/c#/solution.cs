import re

def validate_usr(username):
    return False if not re.search(r"^[a-z0-9_]{4,16}$", username) else True