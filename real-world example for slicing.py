import numpy as np
image = np.array([
    [255, 0, 255],
    [0, 255, 0],
    [255, 0, 255]
                 ])

center = image[1:2, 1:2]
print(center)
