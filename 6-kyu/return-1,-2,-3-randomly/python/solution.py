def one_two_three():
    n = 2*one_two() + one_two() - 2
    while n not in [1,2,3]:
        n = 2*one_two() + one_two() - 2
    return n