def common_ground(s1,s2):
    s11, s22 = set(s1.split()), set(s2.split())    
    match = s11.intersection(s22)
    return  " ".join(sorted(match, key=lambda x: s2.split().index(x))) if match else "death"