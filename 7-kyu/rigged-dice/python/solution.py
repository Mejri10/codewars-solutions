import random

def throw_rigged():
    return 6 if random.random() < 0.22 else random.randint(1, 5)