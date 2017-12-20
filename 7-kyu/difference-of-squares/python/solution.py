def difference_of_squares(x):
    return sum(range(1, x+1))**2 - sum(n**2 for n in range(1, x+1))