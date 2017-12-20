from itertools import product as p

def count_smileys(arr):
    smiles = ["".join(s) for s in p(":;", "-~", ")D")] + ["".join(s) for s in p(":;", ")D")] 
    return sum([1 if s in smiles else 0 for s in arr])