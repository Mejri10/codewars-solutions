def solution(a, b):
    short, long = sorted((a, b), key=len)
    return short + long + short
