import numpy as np

def number(bus_stops):
    return np.sum(np.array(bus_stops)[:,0] - np.array(bus_stops)[:,1])