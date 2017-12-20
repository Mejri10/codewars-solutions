from string import ascii_lowercase as alphabet


def sort_string(s):
    nonEnglishIndex = [i for i in range(len(s)) if s[i].lower() not in alphabet]
    nonEnglishChars = ''.join(s[i] for i in nonEnglishIndex)
    s2 =  "".join(sorted(s, key=lambda x: x.lower())).strip(nonEnglishChars)
    for idx in nonEnglishIndex:
        s2 = s2[:idx] + s[idx] + s2[idx:]
    return s2