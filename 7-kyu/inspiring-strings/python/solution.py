def longest_word(s):
    maxLen = max([len(word) for word in s.split()])
    return [w for w in s.split() if len(w)==maxLen][-1]