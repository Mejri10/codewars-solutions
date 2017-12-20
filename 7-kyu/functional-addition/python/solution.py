def add(n):
    base_value = n
    def add_to_base_value(p):
        nonlocal base_value
        return base_value + p
    return add_to_base_value