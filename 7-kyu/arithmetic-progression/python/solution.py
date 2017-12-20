def arithmetic_sequence_elements(a, r, n):
    arr = range(a, a + r*n, r)
    return ', '.join(map(str, arr))