from string import ascii_lowercase as letters

def lowercase_count(s):
    return sum(1 for _ in s if _ in letters)