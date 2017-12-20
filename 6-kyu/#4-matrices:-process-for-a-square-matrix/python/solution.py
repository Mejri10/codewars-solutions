import numpy as np

def avg_diags(m):
    main_diag_odd = np.diag(m)[1::2]
    sec_diag_even = np.diag(np.fliplr(m))[::-2]
    main_diag_odd = main_diag_odd[main_diag_odd >= 0]
    sec_diag_even = sec_diag_even[sec_diag_even < 0]
    return [round(np.mean(main_diag_odd)) if len(main_diag_odd)>0 else -1, round(abs(np.mean(sec_diag_even))) if len(sec_diag_even)>0 else -1]