import numpy as np
import matplotlib.pyplot as plt

col_tar = (0, 0, 0)    
col_bg  = (255, 255, 0)  


letra6_r = np.array([
    [col_bg[0], col_tar[0], col_tar[0], col_tar[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_tar[0], col_tar[0], col_tar[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_bg[0], col_tar[0], col_tar[0], col_tar[0], col_bg[0]]
], dtype=np.uint8)


letra6_g = np.array([
    [col_bg[1], col_tar[1], col_tar[1], col_tar[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_tar[1], col_tar[1], col_tar[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_bg[1], col_tar[1], col_tar[1], col_tar[1], col_bg[1]]
], dtype=np.uint8)

letra6_b = np.array([
    [col_bg[2], col_tar[2], col_tar[2], col_tar[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_tar[2], col_tar[2], col_tar[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_bg[2], col_tar[2], col_tar[2], col_tar[2], col_bg[2]]
], dtype=np.uint8)

letra6 = np.stack((letra6_r, letra6_g, letra6_b), axis=2)

plt.imshow(letra6)
plt.show()

