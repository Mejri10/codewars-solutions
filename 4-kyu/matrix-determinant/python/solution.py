def cofactor(A, i, j):
    n = len(A)
    B = []
    for ii in range(n):
        row = []
        for jj in range(n):
            if ii != i and jj != j:
                row.append(A[ii][jj])
        if row: B.append(row)
    return B

def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        total = 0
        for i in range(n):
            total += A[0][i] * (-1)**(2 + i) * determinant(cofactor(A, 0, i))
        return total 