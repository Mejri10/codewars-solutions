def closest(lst):
    res = min(lst, key=abs)
    if -res in lst and res != 0:
    	return None
    else:
    	return res