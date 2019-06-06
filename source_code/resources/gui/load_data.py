import numpy as np


def load_data(filename, xcol=0, ycol=1, first_row=0):
    x = []
    y = []
    count = 0
    file = open(filename, 'r')
    for line in file:
        if (count >= first_row):
            str = line.split()
            x.append(float(str[xcol]))
            y.append(float(str[ycol]))
        count += 1
    file.close()
    xv = np.array(x)
    yv = np.array(y)
    return [xv, yv]