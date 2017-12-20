def beasts(heads, tails):
	if 2 * tails <= heads <= 5 * tails:
		return [(5*tails-heads)/3, (heads-2*tails)/3]
	else:
		return "No solutions"