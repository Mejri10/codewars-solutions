def count_arara(n):
	return [' '.join(['adak'] * (n/2)), ' '.join(['adak'] * (n/2) + ['anane'])][ n % 2 != 0]