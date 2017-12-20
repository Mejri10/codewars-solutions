from string import atoi

def my_parse_int(string):
	try: return atoi(string)
	except ValueError: return 'NaN'
	