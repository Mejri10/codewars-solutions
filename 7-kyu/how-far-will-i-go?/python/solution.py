def travel(t_total, t_run, t_rest, speed):
	leftover = t_total % (t_run + t_rest)
	condition = leftover > t_run
	t = t_total/(t_run + t_rest) * t_run + (leftover, t_run)[condition]
	return speed * t
