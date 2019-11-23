def distance(a, b):
    if not a or not b or len(a) != len(b): return -1
    
    return sum((ai-bi)**2 for ai,bi in zip(a,b))**.5