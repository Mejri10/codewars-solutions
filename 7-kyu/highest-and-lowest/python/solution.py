def high_and_low(numbers):
    number = [int(n) for n in numbers.split()]
    return "{} {}".format(max(number), min(number))