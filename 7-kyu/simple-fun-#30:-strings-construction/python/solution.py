from collections import Counter

def strings_construction(A,B):
    a = Counter(A)
    b = Counter(B)
    minimum = []
    for letter in a:
        if letter not in b:
            break
        minimum.append(b[letter]//a[letter])
    else:
        return min(minimum)
    return 0