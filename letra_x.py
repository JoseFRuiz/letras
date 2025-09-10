import numpy as np
import matplotlib.pyplot as plt

col_tar = (0, 0, 0)    
col_bg  = (255, 255, 0) 


letrax_r = np.array([
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_bg[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0], col_bg[0]],
    [col_bg[0], col_bg[0], col_tar[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0]],
    [col_bg[0], col_bg[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_bg[0], col_bg[0], col_tar[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0]],
    [col_bg[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]]
], dtype=np.uint8)


letrax_g = np.array([
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_bg[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1], col_bg[1]],
    [col_bg[1], col_bg[1], col_tar[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1]],
    [col_bg[1], col_bg[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_bg[1], col_bg[1], col_tar[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1]],
    [col_bg[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]]
], dtype=np.uint8)


letrax_b = np.array([
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_bg[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2], col_bg[2]],
    [col_bg[2], col_bg[2], col_tar[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2]],
    [col_bg[2], col_bg[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_bg[2], col_bg[2], col_tar[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2]],
    [col_bg[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]]
], dtype=np.uint8)


letrax = np.stack((letrax_r, letrax_g, letrax_b), axis=2)

plt.imshow(letrax)
plt.show()
