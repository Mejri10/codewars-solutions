import datetime

def days_until_christmas(day):
    xmas = datetime.date(day.year,12,25)
    return (xmas - day).days if xmas >= day else (xmas.replace(year=day.year+1) - day).days