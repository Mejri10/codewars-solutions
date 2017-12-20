from itertools import product

def cartesian_neighbor(x,y):
    return [(xi, yi) for xi, yi in product([x-1, x, x+1], [y-1, y, y+1]) if (xi, yi) != (x, y)]