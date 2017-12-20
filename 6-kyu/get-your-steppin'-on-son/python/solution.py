def word_step(s):
    words = s.split()
    ncolumns = sum([len(word) for word in words[::2]]) - (len(words[::2]) - 1)
    output = []
    trackColumn = 0
    for i, word in enumerate(words):
        if i % 2 == 0:  # horizontal words
            n = len(word)
            word = " "*trackColumn + word + " "*(ncolumns - n - trackColumn)
            trackColumn += n - 1
            output.append(list(word))
        else:  # vertical words
            _word = (word[1:] if i == len(words)-1 else word[1:-1])
            for ch in _word:
                word = " "*trackColumn + ch + " "*(ncolumns - 1 - trackColumn)
                output.append(list(word))       
    return output