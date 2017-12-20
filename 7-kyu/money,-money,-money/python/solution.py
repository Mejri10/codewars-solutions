from math import log, ceil

def calculate_years(p, i, t, d):
	return ceil(log(float(d)/p, 1+i-i*t)) if p < d else 0

