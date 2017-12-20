def sumDig_nthTerm(initVal, patternL, n):
	term = initVal
	pattern = (n/len(patternL) + 1) * patternL
	for i in range(n-1):
		term += pattern[i]
	return sum(int(i) for i in str(term))
