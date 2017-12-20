def epidemic(tm, n, s0, i0, b, a):

	dt = float(tm)/n
	S = [s0] + [0]*n
	I = [i0] + [0]*n
	R = [0] + [0]*n

	for k in range(n):
		S[k+1] = S[k] - dt * b * S[k] * I[k]
		I[k+1] = I[k] + dt * (b * S[k] * I[k] - a * I[k])
		R[k+1] = R[k] + dt * I[k] *a

	return int(max(I))