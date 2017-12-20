from math import pi, log

def circleArea(r):
    try:
        log(r)  # lol
        return round(pi*r**2, 2)
    except:
        return False
  