import numpy as np

def distances_from_average(test_list):
    res =  np.round(-np.array(test_list) + np.mean(test_list), 2)
    return res.tolist()