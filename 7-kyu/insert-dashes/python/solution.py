def insert_dash(num):
	ans = ''
	num = str(num)
	isodd = lambda x: int(x) % 2 != 0
	for i in range(len(num)-1):
		ans += [num[i], num[i] + '-'][isodd(num[i]) and isodd(num[i+1])]
	return ans + num[-1]
