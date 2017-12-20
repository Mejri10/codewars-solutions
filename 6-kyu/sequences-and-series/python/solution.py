import sys
sys.setrecursionlimit(1000000)

def get_score(n):
    if n == 0:
        return 0
    else:
        return get_score(n-1) + n*50