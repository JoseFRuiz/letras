import numpy as np
import matplotlib.pyplot as plt

col_tar = (0, 0, 255)  
col_bg = (0, 128, 0)   

letra_r_8 = np.array([
    [col_bg[0], col_tar[0], col_tar[0], col_tar[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_bg[0], col_tar[0], col_tar[0], col_tar[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_bg[0], col_tar[0], col_tar[0], col_tar[0], col_bg[0]]
], dtype=np.uint8)

letra_g_8 = np.array([
    [col_bg[1], col_tar[1], col_tar[1], col_tar[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_bg[1], col_tar[1], col_tar[1], col_tar[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_bg[1], col_tar[1], col_tar[1], col_tar[1], col_bg[1]]
], dtype=np.uint8)

letra_b_8 = np.array([
    [col_bg[2], col_tar[2], col_tar[2], col_tar[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_bg[2], col_tar[2], col_tar[2], col_tar[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_bg[2], col_tar[2], col_tar[2], col_tar[2], col_bg[2]]
], dtype=np.uint8)

letra = np.stack((letra_r_8, letra_g_8, letra_b_8), axis=2)


plt.imshow(letra)
plt.show()