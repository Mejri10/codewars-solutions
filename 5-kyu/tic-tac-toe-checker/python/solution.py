import numpy as np

def winner(line):
    line = set(line)
    return 0 if len(line) > 1 else list(line)[0]

def isSolved(board):
    board = np.array(board)
    lines = np.concatenate((board,  # rows
                            np.transpose(board),  # columns
                            [np.diag(board)],  # main diagonal
                            [np.diag(np.rot90(board))]  # second diagonal
                          ))
    for line in lines:
        if winner(line):
            return winner(line)
    return -1 if 0 in board else 0
    
