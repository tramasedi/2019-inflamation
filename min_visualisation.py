import numpy as np 
data = np.loadtxt(
	fname = 'data/inflammation-01-.csv'
	delimiter = ','
)
import matplotlib as plt 
min_inflammation = np.mean(
	data,
	axis=0
)

