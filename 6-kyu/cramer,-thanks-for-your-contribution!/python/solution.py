import numpy as np
from numpy.linalg import det as determinant

def cramer_solver(matrix, vector):
    matrix, vector = np.array(matrix), np.array(vector)
    nRows, nCols = matrix.shape
    vectorDim = vector.size
    
    if nRows != nCols or vectorDim != nRows:
        return "Check entries"
        
    det = round(determinant(matrix))
    dets = []
    for i in range(vector.size):
        copy = matrix.copy()
        copy[:, i] = vector
        dets.append(round(determinant(copy)))
    
    if det == 0:
        if all([det_i == 0 for det_i in dets]):
            return "Indeterminate or Unsolvable"
        else: 
            return "Unsolvable"
    else:
        return [det, *dets]
        