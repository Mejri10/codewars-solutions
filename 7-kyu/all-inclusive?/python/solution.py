def contain_all_rots(s, arr):    
    rots = [s[x:]+s[:x] for x in range(len(s))]    
    matches = [i in arr for i in rots]    
    return False if False in matches else True
        