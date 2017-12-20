from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    freqs = Counter(word)
    return ''.join([')' if freqs[w] > 1 else '(' for w in word])