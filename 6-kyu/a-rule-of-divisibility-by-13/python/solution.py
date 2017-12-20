def thirt(n):
    pattern = (1, 10, 9, 12, 3, 4)
    last = next_ = count = 0
    while True:
        while n > 0:
            next_ += (n % 10) * pattern[count % len(pattern)]
            n = n // 10
            count += 1
        if next_ == last:
            break
        else:
            last = n = next_
            next_ = count = 0
    return next_
        