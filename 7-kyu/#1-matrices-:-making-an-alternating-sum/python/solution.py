def score_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    total = 0
    for i in range(0, m):
        for j in range(0, n):
            total += (-1)**(i+j+2) * matrix[i][j]
    return total            
    
    
