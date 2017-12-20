from math import pi

def sum_circles(*args):
    return "We have this much circle: {}".format(int(round(sum(map(lambda d: pi/4*d**2, args)))))