def mxdiflg(a1, a2):	
	if not a1 or not a2: return -1
	min1, max1 = min(len(x) for x in a1), max(len(x) for x in a1)
	min2, max2 = min(len(x) for x in a2), max(len(x) for x in a2)
	return max(max1 - min2, max2 - min1)