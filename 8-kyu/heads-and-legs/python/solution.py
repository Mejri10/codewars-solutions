def animals(heads, legs):
    chickens = 2*heads - legs/2
    cows = legs/2 - heads
    if legs/2 != legs//2 or chickens < 0 or cows < 0:
        return 'No solutions'
    else:
        return (chickens, cows)