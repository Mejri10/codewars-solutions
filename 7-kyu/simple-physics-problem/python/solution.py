def solveit(vi, vf, t):
    return [round((vf - vi)/t, 2), round(vi*t + 0.5*(vf - vi)/t*(t**2), 2)] if vf > vi else []