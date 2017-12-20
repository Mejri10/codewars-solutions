from collections import Counter

def first_non_repeating_letter(string):
    c = Counter(string)
    nonrepetitive = [k for k, v in c.items() if v == 1]
    nonrepetitive = [k for k in nonrepetitive if not k.isalpha()] + \
                    [k for k in nonrepetitive if k.swapcase() not in string]
    if nonrepetitive:
        return min(nonrepetitive, key=string.index)
    else:
        return ""