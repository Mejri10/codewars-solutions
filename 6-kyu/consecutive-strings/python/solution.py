def longest_consec(arr, k):
	if len(arr) == 0  or k > len(arr) or k <= 0:
		return ''
	arr_len = [len(i) for i in arr]
	index, total = 0, 0
	for i in range(len(arr) - (k-1)):
		partial_sum = sum(arr_len[i:i+k])
		if partial_sum > total:
			total = partial_sum
			index = i
	return ''.join(arr[index:index+k])
        
    	
    	
