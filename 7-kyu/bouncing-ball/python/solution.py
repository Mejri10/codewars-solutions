from math import log, ceil

def bouncing_ball(initial, proportion):
    return ceil(log(1/initial, proportion))