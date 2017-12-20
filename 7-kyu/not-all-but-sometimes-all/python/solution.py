def remove(text, what):
    text = list(text)
    for letter in what:
        for times in range(what[letter]):
            try:
                text.remove(letter) 
            except:
                pass
    return ''.join(text)

   