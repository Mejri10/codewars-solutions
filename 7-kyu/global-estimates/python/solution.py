def global_estimate(estimates):
    best = worst = 0
    for b, w in estimates:
        best += b
        worst += w
    return (best, 0.5*(best + worst), worst)