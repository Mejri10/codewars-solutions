def greek_comparator(lhs, rhs):
	print lhs, rhs
	s = cmp(greek_alphabet.index(lhs), greek_alphabet.index(rhs))
	if s < 0:
		return s
	elif s > 0:
		return "result should be positive"
	else:
		return 0