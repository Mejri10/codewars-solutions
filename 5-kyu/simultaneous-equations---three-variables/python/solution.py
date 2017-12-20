"""
Ugliest Algortithm Ever
Feel free to read this Abomination
"""

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

def det(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    else:
        total = 0
        for i in range(n):
            total += A[0][i] * (-1)**(2 + i) * det(cofactor(A, 0, i))
        return total    


def solve_eq(eq):
    detEq = det([eq[i][:3] for i in range(len(eq))])
    x = det([[eq[i][-1]] + eq[i][1:len(eq)] for i in range(len(eq))])/detEq
    y = det([[eq[i][0]] + [eq[i][-1]] + [eq[i][2]] for i in range(len(eq))])/detEq 
    z = det([[eq[i][0]] + [eq[i][1]] + [eq[i][-1]] for i in range(len(eq))])/detEq   
    return[x, y, z]