def you_are_a_cube(cube):
    n = cube**(1/3)
    return abs(n - round(n)) < 1e-10