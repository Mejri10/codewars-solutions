from fractions import gcd
from functools import reduce

def final_attack_value(x,monster_list):
    return reduce(lambda x,y: x+y if x > y else x + gcd(x,y), [x] + monster_list)