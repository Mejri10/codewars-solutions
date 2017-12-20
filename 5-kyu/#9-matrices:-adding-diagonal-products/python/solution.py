import numpy as np

def sum_main_diagonal(matrix):
    n = matrix.shape[0]
    return sum(np.prod(np.diagonal(matrix, i)) for i in range(-n+1, n))    

def sum_prod_diags(matrix):
    matrix_np = np.array(matrix)
    sum1 = sum_main_diagonal(matrix_np)
    sum2 = sum_main_diagonal(np.fliplr(matrix_np))
    return sum1 - sum2