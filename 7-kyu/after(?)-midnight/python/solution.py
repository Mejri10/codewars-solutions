def day_and_time(mins):
    import datetime     
    
    someSunday = datetime.datetime(2016, 5, 1, 0, 0, 0)
    minutes = datetime.timedelta(minutes=mins)
    newDatetime = someSunday + minutes
    return newDatetime.strftime('%A %H:%M')