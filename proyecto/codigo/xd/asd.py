import numpy as np 
a = np.array([[1, 2, 0, 0],
              [5, 3, 0, 4],
              [0, 0, 0, 7],
              [9, 3, 0, 0]])
k = np.array([[1,1,1],[1,1,0],[1,0,0]])

print(a.shape)
print(k.shape)

from scipy import ndimage
ndimage.convolve(a, k, mode='constant', cval=0.0)