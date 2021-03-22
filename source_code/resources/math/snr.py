import numpy as np


def calculate_snr(s, nv):
    n_mean = np.mean(nv)
    nv_zero_mean = nv - n_mean * np.ones(nv.size)
    n_std = np.std(nv_zero_mean)
    snr = s / n_std
    return snr, n_std