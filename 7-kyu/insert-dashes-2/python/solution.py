def insert_dash2(num):
	isEven = lambda x: x % 2 == 0 and x != 0
	isOdd = lambda x: x % 2 != 0 and x!= 0
	ans = ''
	num = str(num)
	for i in range(len(num) - 1):
		if isEven(int(num[i])) and isEven(int(num[i+1])):
			ans += num[i] + '*'
		elif isOdd(int(num[i])) and isOdd(int(num[i+1])):
			ans += num[i] + '-'
		else:
			ans += num[i]
	return ans + num[-1]
        