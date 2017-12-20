def get_count(words=''):
	if not isinstance(words, str):
		return {"vowels": 0, "consonants": 0}
	else:
		words = words.lower()
		vowels = 'aeiou'
		consonants = 'bcdfghjklmnpqrstvwxyz'
		nVowels = len(words) - len(words.translate(None, vowels))
		nConsonants = len(words) - len(words.translate(None, consonants))
		return {"vowels": nVowels, "consonants": nConsonants}