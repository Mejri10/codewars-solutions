def count_vowels(s=''):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if isinstance(s, str):
        return sum(1 if c.lower() in vowels else 0 for c in s)
    else:
        return None