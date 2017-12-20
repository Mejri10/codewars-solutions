def winner(candidates):
	# Check required conditions
	if len(candidates) != 3:
		return False

	for candidate in candidates:
		if not candidate.has_key('name') or not candidate.has_key('scores'):
			return False

	for candidate in candidates:
		if not(0 < len(candidate['scores']) < 3) :
			return False

	for candidate in candidates:
		for score in candidate['scores']:
			if score % 5 != 0 or not(5 <= score <= 100):
				return False

	possibleWinners = filter(lambda x: sum(x['scores']) <= 100, candidates)
	if not possibleWinners:
		return False
	else:
		max_score = max(map(lambda x: sum(x['scores']), possibleWinners))
		return filter(lambda x: sum(x['scores']) == max_score, possibleWinners)[0]['name']
