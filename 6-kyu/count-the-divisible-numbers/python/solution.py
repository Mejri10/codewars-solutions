def divisible_count(x,y,k):
    return y//k - x//k + (1 if x % k == 0 else 0)