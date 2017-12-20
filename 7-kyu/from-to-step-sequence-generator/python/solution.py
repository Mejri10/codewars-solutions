def generator (s, e, h):
	if s <= e:
		return range(s, e+1, h) if h > 0 else []
	else:
		return range(s, e-1, -h) if h > 0 else []
        