def is_narcissistic(i):
	digitsPowered = [int(j)**len(list(str(i))) for j in list(str(i))]
	return i == sum(digitsPowered)
    