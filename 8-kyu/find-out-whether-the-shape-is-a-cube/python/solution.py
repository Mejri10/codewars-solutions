def cube_checker(volume, side):
    if side < 0 or volume < 0:
        return False
    else:
        return side * side * side ==  volume