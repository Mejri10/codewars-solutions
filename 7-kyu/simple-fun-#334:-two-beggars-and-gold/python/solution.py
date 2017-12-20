def distribution_of(golds):
    goldA = 0
    goldB = 0
    turn = 0
    while len(golds) > 0:
        a, b = golds[0], golds[-1]
        if turn % 2 == 0:
            if a >= b:
                goldA += a
                golds = golds[1:]
            else:
                goldA += b
                golds = golds[:-1]
        else:
            if a >= b:
                goldB += a
                golds = golds[1:]
            else:
                goldB += b
                golds = golds[:-1]
        turn += 1
    return [goldA, goldB]
                