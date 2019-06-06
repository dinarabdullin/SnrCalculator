import os
import sys
import math
from math import factorial
import numpy as np


def savitzky_golay_filter(x, window_size, order, deriv=0, rate=1):
	try:
		window_size = np.abs(np.int(window_size))
		order = np.abs(np.int(order))
	except (ValueError,IOError):
		raise ValueError("Window_size and order have to be of type int")
	if window_size % 2 != 1 or window_size < 1:
		raise TypeError("Window_size size must be a positive odd number")
	if window_size < order + 2:
		raise TypeError("Window_size is too small for the polynomials order")
	order_range = range(order+1)
	half_window = (window_size -1) // 2
	# Precompute coefficients
	b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
	m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
	# Pad the signal at the extremes with values taken from the signal itself
	firstvals = x[0] - np.abs( x[1:half_window+1][::-1] - x[0] )
	lastvals = x[-1] + np.abs(x[-half_window-1:-1][::-1] - x[-1])
	x = np.concatenate((firstvals, x, lastvals))
	y = np.convolve(m[::-1], x, mode='valid')
	return y