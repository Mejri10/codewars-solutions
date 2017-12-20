def resistor_parallel(*res):
    rightHandSide = sum([1/float(r) for r in res])
    return 1/rightHandSide