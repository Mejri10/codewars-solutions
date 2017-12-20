def length_of_sequence(arr,n):
	found = []
	for i in range(len(arr)):
		if arr[i] == n: found.append(i)
	return found[1] - found[0] + 1 if len(found) == 2 else 0
