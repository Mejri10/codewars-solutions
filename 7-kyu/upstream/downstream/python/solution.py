def time(distance,boat_speed,stream):
    stream_speed = int(stream.split()[1]) * (-1)**stream.startswith('U')
    return round(distance/(boat_speed + stream_speed), 2)