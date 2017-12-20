def find_digit(num, nth):
    return int(str(abs(num))[::-1].ljust(nth, '0')[nth-1]) if nth > 0 else -1