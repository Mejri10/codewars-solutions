def to_weird_case(string):
	ans = []
	for word in string.split():
		ans2 = []
		for i, c in enumerate(word):
			ans2.append([c.upper(), c.lower()][i % 2])
		ans.append(''.join(ans2))
	return ' '.join(ans) 