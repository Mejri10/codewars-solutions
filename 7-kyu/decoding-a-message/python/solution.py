from string import ascii_lowercase as alpha

def decode(message):
    decoder = dict(zip(alpha[::-1] + ' ', alpha + ' '))
    return ''.join(decoder[c] for c in message)
    