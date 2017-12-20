def validate_code(code):
    return any(str(code).startswith(str(i)) for i in range(1, 4))