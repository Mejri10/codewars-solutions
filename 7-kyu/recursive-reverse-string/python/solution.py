def reverse(s):
	return s[-1] + (reverse(s[:-1]) if len(s) > 1 else '')