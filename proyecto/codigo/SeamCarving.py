import sys
import numpy as np
from scipy.ndimage import convolve
import numba

class SC:
    def __init__(self, data):
        self.nparr = np.array(data)
        self.scale_c = 0.70
        self.crop_c()
    
    def return_list(self):
        return self.nparr.tolist()
    
    def calc_energy(self):
        filter_du = np.array([
            [1.0, 2.0, 1.0],
            [0.0, 0.0, 0.0],
            [-1.0, -2.0, -1.0],
        ])
        
        filter_dv = np.array([
            [1.0, 0.0, -1.0],
            [2.0, 0.0, -2.0],
            [1.0, 0.0, -1.0],
        ])
        
        
        self.nparr = self.nparr.astype('float32')
        #print(self.nparr.shape, self.nparr.ndim)
        #print(filter_dv.shape, filter_dv.ndim)

        energy_map = np.absolute(convolve(self.nparr, filter_du, mode='constant', cval=0.0)) + np.absolute(convolve(self.nparr, filter_dv, mode='constant', cval=0.0))
        
        return energy_map

    def crop_c(self):
        r, c = self.nparr.shape
        new_c = int(self.scale_c * c)

        for i in range(c - new_c):
            self.carve_column()

    @numba.jit
    def carve_column(self):
        r, c = self.nparr.shape

        M, backtrack = self.minimum_seam()
        mask = np.ones((r, c), dtype=np.bool)

        j = np.argmin(M[-1])
        for i in reversed(range(r)):
            mask[i, j] = False
            j = backtrack[i, j]

        #print("mask")
        #print(self.nparr.shape, self.nparr.ndim)
        
        #print("Arr")
        #print(self.nparr.shape, self.nparr.ndim)
        # mask = np.stack([mask], axis=0)
        self.nparr = self.nparr[mask]
        
        #print("Arr2")
        #print(self.nparr.shape, self.nparr.ndim)
        self.nparr = self.nparr.reshape((r, c - 1))
        
        #print("Arr3")
        #print(self.nparr.shape, self.nparr.ndim)

    @numba.jit
    def minimum_seam(self):
        r, c = self.nparr.shape
        energy_map = self.calc_energy()

        M = energy_map.copy()
        backtrack = np.zeros_like(M, dtype=np.int)

        for i in range(1, r):
            for j in range(0, c):
                if j == 0:
                    idx = np.argmin(M[i-1, j:j + 2])
                    backtrack[i, j] = idx + j
                    min_energy = M[i-1, idx + j]
                else:
                    idx = np.argmin(M[i - 1, j - 1:j + 2])
                    backtrack[i, j] = idx + j - 1
                    min_energy = M[i - 1, idx + j - 1]

                M[i, j] += min_energy

        return M, backtrack
