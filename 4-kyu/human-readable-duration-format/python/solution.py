def seconds_to_time_units(total_seconds):
    years, days_left = divmod(total_seconds, 60*60*24*365)
    days, hours_left = divmod(days_left, 60*60*24)
    hours, minutes_left = divmod(hours_left, 60*60)
    minutes, seconds = divmod(minutes_left, 60)
    return years, days, hours, minutes, seconds

def format_duration(total_seconds):
    if not total_seconds:
        return 'now'
    else:
        time_units = seconds_to_time_units(total_seconds)
        time_units_str = ["year", "day", "hour", "minute", "second"]
        res = []
        for value, name in zip(time_units, time_units_str):
            if value == 0:
                continue
            else:
                name = name + 's' * (value > 1)
                res.append("{} {}".format(value, name))
        return ', '.join(res[:-1]) + ' and ' + res[-1] if len(res) > 1 else res[0]