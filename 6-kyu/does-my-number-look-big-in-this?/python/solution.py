def narcissistic(value):
    n = len(str(value))
    return sum(int(d)**n for d in str(value)) == int(value)