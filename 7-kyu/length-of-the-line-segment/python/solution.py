import numpy as np
from numpy.linalg import norm

def length_of_line(a):
    a = np.array(a)
    return '{:.2f}'.format(norm(a[1, :] - a[0, :]))
