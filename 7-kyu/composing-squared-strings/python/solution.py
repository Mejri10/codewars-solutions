def compose(s1, s2):
	t = [a + b for a, b in zip(s1.split('\n'), s2.split('\n')[::-1])]
	return '\n'.join([a[:i+1] + a[len(t):len(a)- i] for i, a in enumerate(t)])