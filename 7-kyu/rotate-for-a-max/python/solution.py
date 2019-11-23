"""
    Not Space & Time Optimized but what the hell
"""

def max_rot(n):
    return max(map(int, rotations(str(n))))

def rotations(n, offset=0):
    if len(n) == offset: return []
    
    nRotated = n[0:offset] + rotate(n[offset:])
    return ([n, nRotated] if offset==0 else [nRotated]) + rotations(nRotated, offset+1)

def rotate(n):
    return (n + n)[1:(len(n)+1)]