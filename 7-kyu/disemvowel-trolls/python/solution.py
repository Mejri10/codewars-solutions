def disemvowel(string):
    vowels = 'aeiou'
    new_string = []
    for letter in string:
        if letter.lower() not in vowels: new_string.append(letter)
    return ''.join(new_string)