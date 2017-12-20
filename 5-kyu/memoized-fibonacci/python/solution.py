memoized_fib = {0: 0, 1: 1}

def fibonacci(n):
    if n in memoized_fib:
        return memoized_fib[n]
    else:
        memoized_fib[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memoized_fib[n]