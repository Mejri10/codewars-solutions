import numpy as np

def centroid(c):
    return np.round(np.mean(c, 0), 2).tolist()
