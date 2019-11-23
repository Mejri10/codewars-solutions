def solution(a, b):
    short, long = min((a, b), key=len), max((a, b), key=len)
    return short + long + short
