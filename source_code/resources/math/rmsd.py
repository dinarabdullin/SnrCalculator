import numpy as np


def calculate_rmsd(s1, s2):
    rmsd = 0.0
    for i in range(s1.size):
        rmsd += (s1[i] - s2[i])**2
    rmsd /= float(s1.size)
    rmsd = np.sqrt(rmsd)
    return rmsd