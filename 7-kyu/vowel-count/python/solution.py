def getCount(inputStr):
    return sum(1 for c in inputStr if c in 'aeiou')