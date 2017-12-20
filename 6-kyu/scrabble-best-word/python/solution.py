def get_best_word(points, words):
    points_per_letter = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", points))
    points_per_word = [sum([points_per_letter[letter] for letter in word]) for word in words] 
    max_points = max(points_per_word)
    return words.index(min([word for i, word in enumerate(words) if points_per_word[i] == max_points], key=len))
    
