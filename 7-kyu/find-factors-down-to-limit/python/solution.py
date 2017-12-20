def factors(integer, limit):
    return [n for n in range(limit, integer + 1) if integer % n == 0]