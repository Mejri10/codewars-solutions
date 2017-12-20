def vert_mirror(s):
    return '\n'.join(si[::-1] for si in s.split('\n'))
    
def hor_mirror(s):
    return '\n'.join(s.split('\n')[::-1])

def oper(fct, s):
    return fct(s)