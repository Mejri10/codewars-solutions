import numpy as np

def better_than_average(class_points, your_points):
    return your_points > np.mean(class_points)