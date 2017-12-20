def get_users_ids(string):
	return [s.lower().replace('#', '').replace('uid', '', 1).strip() for s in string.split(',')]
	