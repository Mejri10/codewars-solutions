def year_days(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        isleap = True
    else:
        isleap = False
    return "{} has {} days".format(year, (365, 366)[isleap])