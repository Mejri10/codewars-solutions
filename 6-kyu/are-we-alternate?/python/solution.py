def isAlt(s):
    vowels = 'aeiou'
    rule = lambda x,y : x in vowels and y not in vowels or x not in vowels and y in vowels
    return all(rule(s[i], s[i+1]) for i in range(len(s) - 1))