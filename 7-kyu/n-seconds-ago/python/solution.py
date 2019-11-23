from datetime import datetime, timedelta

def seconds_ago(s,n):
    time = datetime.strptime(s, "%Y-%m-%d %H:%M:%S") - timedelta(seconds=n)
    return f"{str(time.year).zfill(4)}{datetime.strftime(time , '-%m-%d %H:%M:%S')}"