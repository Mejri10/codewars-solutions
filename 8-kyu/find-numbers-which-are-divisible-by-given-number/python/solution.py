def divisible_by(numbers, divisor):
    return filter(lambda x: x % divisor == 0, numbers)