from math import log, ceil
import datetime

def date_nb_days(a0, a, p):
	n = ceil(log(float(a)/a0, 1 + float(p)/36000))
	today = datetime.date(2016, 1, 1)
	finalDay = today + datetime.timedelta(days=n)	
	return str(finalDay)