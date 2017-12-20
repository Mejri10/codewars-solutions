def convert_to_mixed_numeral(parm):
    n, d = [int(i) for i in parm.split('/')]
    if abs(n) < d: 
        return parm
    else:
        a, b = divmod(abs(n), d)
        if b == 0: return "-" * (n < 0) + "%d" % a
        return "-" * (n < 0) + "%d %d/%d" % (a, b, d) 
    