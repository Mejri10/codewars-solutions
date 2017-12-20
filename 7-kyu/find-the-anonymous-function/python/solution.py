def find_function(func,arr):
	for f in func:
		try: return filter(f, arr)
		except: continue