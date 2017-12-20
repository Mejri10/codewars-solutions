import re

def get_terms(pol):
	return re.findall(r"([-+]?\d*\w+)", pol)

def get_coefs_and_mon(term):
	coef, mon = re.findall(r"([+-]?\d*)(\w+)", term)[0]
	if not coef or coef == '+':
		coef = 1
	elif coef == '-':
		coef = -1
	else:
		coef = int(coef)
	return coef, ''.join(sorted(mon))

def format_mon(coef, mon):
	if coef == 0:
		return ''
	else:		
		sign = ('-', '+')[coef > 0]
		return "{}{}{}".format(sign, abs(coef) if abs(coef) > 1 else '', mon)

def simplify(pol):
	monomials = {}
	for term in get_terms(pol):
		coef, mon = get_coefs_and_mon(term)
		monomials[mon] = monomials.get(mon, 0) + coef
	res = ""
	for mon, coef in sorted(sorted(monomials.items()), key=lambda x: len(x[0])):
		res += format_mon(coef, mon)
	return res.lstrip('+')