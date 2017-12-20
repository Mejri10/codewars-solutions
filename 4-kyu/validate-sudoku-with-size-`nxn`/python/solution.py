import numpy as np

class Sudoku(object):

    def __init__(self, sudoku):
        self.sudoku = np.array(sudoku)
        
    def is_valid(self):
        N = self.sudoku.shape[0]
        if self.sudoku.shape != (N, N):
            return False
        elif not all(type(i) == np.int64 for i in self.sudoku.flatten()):
            return False
        else:
            n = int(N**.5)
            validation_set = set(range(1, N+1))
            rows = all(set(self.sudoku[i, :]) == validation_set for i in range(N))
            cols = all(set(self.sudoku[:, i]) == validation_set for i in range(N))
            squares = all(set(self.sudoku[i:i+n, j:j+n].reshape(1, N)[0]) == validation_set
                          for i in range(0, N, n) for j in range(0, N, n)
                          )
            return rows and cols and squares  