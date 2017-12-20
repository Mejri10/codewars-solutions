def extended_gcd(a, b):
	s, s_old = 0, 1
	t, t_old = 1, 0
	r, r_old = b, a
	while r != 0:
		quotient = r_old / r
		r_old, r = r, (r_old - quotient * r)
		s_old, s = s, (s_old - quotient * s)
		t_old, t = t, (t_old - quotient * t)
	return s_old, t_old, r_old

def inverseMod(a, m):
	s, t, r = extended_gcd(a, m)
	if s < 0: s = m + s
	return None if r != 1 else s
