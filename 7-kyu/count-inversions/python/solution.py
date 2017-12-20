def count_inversion(sequence):
	inversions = 0
	arr = list(sequence)
	arrSorted = sorted(sequence)
	while arr != arrSorted:
		for i in range(len(arr) - 1):
			if arr[i+1] < arr[i]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				inversions += 1
	return inversions		