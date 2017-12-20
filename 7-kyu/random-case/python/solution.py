import random

def random_case(x):
    return ''.join(map( lambda y: y.lower() if random.randint(0,1) == 1 else y.upper() , x))