def match_arrays(v, r):
    res = 0
    for n in v:
        if n in r:
            res += 1
    return res            
  

# DON'T remove
verbose = False # set to True to diplay arrays being tested in the random tests