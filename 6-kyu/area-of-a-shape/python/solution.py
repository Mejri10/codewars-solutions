import numpy as np

def area_of_the_shape(f):
    dx = 1e-3
    dy = 1e-3
    total = 0
    for xi in np.arange(dx/2, 1, dx):
        for yi in np.arange(dy/2, 1, dy):
            total += f(xi, yi)*dx*dy
    return total
