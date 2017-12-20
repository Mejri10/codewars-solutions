from itertools import product


def neighbours_index(index, size):
    i, j = index
    nrows, ncolumns = size
    idxs = product([i, i-1, i+1], [j, j-1, j+1])    
    idxs = list(filter(lambda x: x[0]>=0 and x[0]<nrows and x[1]>=0 and x[1]<ncolumns, idxs))
    idxs.remove((i, j))
    return idxs

def size(matrix):
    return (len(matrix), len(matrix[0]))

def minesweeper(matrix):
    dim = size(matrix)
    output = [[] for _ in range(dim[0])]
    for i in range(dim[0]):
        for j in range(dim[1]):     
            output[i].append(sum([matrix[ii[0]][ii[1]] for ii in neighbours_index((i, j), dim)]))
    return output