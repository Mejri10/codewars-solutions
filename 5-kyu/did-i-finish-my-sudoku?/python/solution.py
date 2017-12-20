import numpy as np

def done_or_not(board):
    board = np.array(board)
    N, n = 9, 3
    validation_set = set(range(1, N+1))
    rows = all(set(board[i, :]) == validation_set for i in range(N))
    cols = all(set(board[:, i]) == validation_set for i in range(N))
    squares = all(set(board[i:i+n, j:j+n].reshape(1, N)[0]) == validation_set
                  for i in range(0, N, n) for j in range(0, N, n)
                  )
    return ("Try again!", "Finished!")[rows and cols and squares] 