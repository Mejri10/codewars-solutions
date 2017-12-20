def unused_digits(*args):
	digits = '0123456789'
	ans = ''
	for i in digits:
		if i not in str(args):
			ans += i
	return ans
            
    	