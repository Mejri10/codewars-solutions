def solution(n):
    d = n - int(n)
    d = 0 if d < 0.25 else 0.5 if d < 0.75 else 1
    return int(n) + d