from math import pi, sqrt

def ellipse(a, b):
    area = pi * a * b
    perimeter = pi * (3/2 * (a + b) - sqrt(a * b))
    return f"Area: {round(area, 1)}, perimeter: {round(perimeter, 1)}"