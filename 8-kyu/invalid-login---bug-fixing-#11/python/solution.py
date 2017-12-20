def validate(username, password):
    validator = Validator()
    return validator.login(username, password.replace('/', '').replace('\\', ''))