def count_matches(a, b):
	count = 0
	for i, s in enumerate(a):
		if b[i] == s:
			count += 1
		else:
			break
	return count

def string_suffix(str_):
    total = 0
    for i in range(len(str_)):
    	total += count_matches(str_[i:], str_)
    return total