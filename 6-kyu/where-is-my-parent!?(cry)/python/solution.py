from string import ascii_lowercase as l
from string import ascii_uppercase as u

a = dict(zip(u, range(0, 2*26, 2)))
b = dict(zip(l, range(1, 2*26+1, 2)))
z = a.copy()
z.update(b)

def find_children(d):
    return ''.join(sorted(d, key=lambda x: z[x]))
    