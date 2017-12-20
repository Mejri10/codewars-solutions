import numpy as np

def up_down_col_sort(matrix):
    m = np.array(matrix)
    nrows, ncols = m.shape
    res = np.zeros((nrows, ncols))
    m_flat = np.sort(m.flatten())
    for i in range(ncols):
        res[:, i] = m_flat[nrows*i: nrows*(i+1)][::(-1)**i]
    return res.tolist()