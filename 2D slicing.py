import numpy as np
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
              ])
print(arr2[1])#row slicing
print(arr2[:, 1])# COLUM slicing
print(arr2[0:2, 1:3])# extract subarray