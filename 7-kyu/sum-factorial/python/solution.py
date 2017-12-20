def fact(n):
	if n == 0: return 1
	else: return n * fact(n-1)

def sum_factorial(lst):
	return sum(map(lambda x: fact(x), lst))