import numpy as np


def calculate_modulation_depth(s):
    return (np.amax(s) - np.mean(s[-10:]))