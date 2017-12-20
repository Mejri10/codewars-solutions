def calculate(n1, n2, o):
	if o == 'add': 		return bin(int(n1, 2) + int(n2, 2)).replace('0b', '')
	if o == 'subtract': return bin(int(n1, 2) - int(n2, 2)).replace('0b', '')
	if o == 'multiply': return bin(int(n1, 2) * int(n2, 2)).replace('0b', '')