def nb_year(p0, percent, aug, p):
    func = lambda n: p0*(1+percent/100)**n + sum(aug * (1+percent/100)**i for i in range(n))
    years = 0
    while func(years) < p:
        years += 1
    return years