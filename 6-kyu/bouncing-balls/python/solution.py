from math import log, floor

def bouncingBall(h, bounce, window):
	if h > 0 and 0 < bounce < 1 and window < h:
		return 2 * floor(log(window/h, bounce)) + 1
	else:
		return -1