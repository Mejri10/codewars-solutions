def sentencify(words):
    sentence = ' '.join(words)
    return sentence[0].upper() + sentence[1:] + '.'