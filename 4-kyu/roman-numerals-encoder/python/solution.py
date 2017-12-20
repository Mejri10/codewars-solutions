conversion = {1000: "M", 900: "CM", 500: "D",
			  400: "CD", 100: "C", 90: "XC", 
			  50: "L", 40: "XL", 10: "X",
			  9: 'IX', 5: "V", 4: "IV", 1: "I"}

def solution(n):
	res = ''
	for key in sorted(conversion, reverse=True):
		q, r = divmod(n, key)
		if q == 0:
			continue
		else:
			res += q * conversion[key]
			n = r
			if n == 0: break
	return res