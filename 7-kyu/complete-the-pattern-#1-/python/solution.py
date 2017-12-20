def pattern(n):
	ans = ""
	for i in range(1, n + 1):
		ans += i*str(i) + '\n'
	return ans.rstrip('\n')
    