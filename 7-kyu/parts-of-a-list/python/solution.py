def partlist(arr):
	ans = []
	for i in range(len(arr)-1):
		ans.append((' '.join(arr[:i+1]), ' '.join(arr[i+1:])))
	return ans