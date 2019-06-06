import numpy as np


def mirror_data(x, y):
	xm = np.append((-1) * x[::-1], x)
	ym = np.append(y[::-1], y)
	return [xm, ym]