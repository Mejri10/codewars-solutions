def decodeMorse(txt):
    words = [word.split() for word in txt.strip().split('   ')]
    return ' '.join([''.join([MORSE_CODE[ch] for ch in word]) for word in words])