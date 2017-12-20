def gifts(number):
    choices = bin(number)[2:].zfill(10)[::-1]
    toys = [gift for n, gift in sorted(GIFTS.items())]
    return sorted([toy for i, toy in enumerate(toys) if choices[i] == '1'])
