import numpy as np

def clean_mean(sample, cutoff):
    mean, std = np.mean(sample), np.std(sample)
    newSample = [n for n in sample if mean - cutoff*std <= n <= mean + cutoff*std]
    if len(sample) == len(newSample):
        return round(mean, 2)
    else:
        return clean_mean(newSample, cutoff)