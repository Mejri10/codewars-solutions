def is_magical(sq):
    rows = all(sum(sq[3*i:3*i+3]) == 15 for i in range(3))
    cols = all(sum(sq[i::3]) == 15 for i in range(3))
    diag1 = sum(sq[::4]) == 15
    diag2 = sum(sq[2:7:2]) == 15
    return rows and cols and diag1 and diag2