import numpy as np

def rotate_like_a_vortex(matrix):
    m = np.array(matrix)
    res = np.zeros(m.shape)
    size = m.shape[0]
    for i in range(size//2 + 1):
        res[i:size-i, i:size-i] = np.rot90(m[i:size-i, i:size-i], i+1)
    return res.tolist()