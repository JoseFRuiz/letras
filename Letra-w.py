import numpy as np
import matplotlib.pyplot as plt

col_tar = (0, 0, 0)    
col_bg  = (255, 255, 255) 


letraW_r = np.array([
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_tar[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_tar[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_tar[0], col_bg[0], col_tar[0], col_tar[0]],
    [col_bg[0], col_tar[0], col_bg[0], col_tar[0], col_bg[0]]
], dtype=np.uint8)


letraW_g = np.array([
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_tar[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_tar[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_tar[1], col_bg[1], col_tar[1], col_tar[1]],
    [col_bg[1], col_tar[1], col_bg[1], col_tar[1], col_bg[1]]
], dtype=np.uint8)


letraW_b = np.array([
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_tar[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_tar[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_tar[2], col_bg[2], col_tar[2], col_tar[2]],
    [col_bg[2], col_tar[2], col_bg[2], col_tar[2], col_bg[2]]
], dtype=np.uint8)


letraW = np.stack((letraW_r, letraW_g, letraW_b), axis=2)

plt.imshow(letraW)
plt.show()
