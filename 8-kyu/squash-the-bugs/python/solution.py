def find_longest(string):
    return len(max(string.split(), key=len))