def pattern(n):
	ans = ''
	for i in range(n):
		ans += ''.join([str(i) for i in range(n,i,-1)]) + '\n'
	return ans.rstrip('\n')