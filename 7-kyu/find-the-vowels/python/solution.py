def vowel_indices(word):
    vowels = 'aeiouy'
    vowels_index = []
    for index,letter in enumerate(word.lower()):
        if letter in vowels:
            vowels_index.append(index+1)
    return vowels_index