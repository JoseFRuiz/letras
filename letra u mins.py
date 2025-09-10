import numpy as np
import matplotlib.pyplot as plt


col_tar = (0, 0, 255)  
col_bg = (0, 128, 0)   

# u

letra_r_u = np.array([
    [col_bg[0], col_bg[0], col_bg[0], col_bg[0],  col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_bg[0], col_tar[0], col_tar[0], col_tar[0], col_bg[0]]
], dtype=np.uint8)

letra_g_u = np.array([
    [ col_bg[1], col_bg[1], col_bg[1], col_bg[1],  col_bg[1]],
    [col_bg[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_bg[1], col_tar[1], col_tar[1], col_tar[1], col_bg[1]]
], dtype=np.uint8)

letra_b_u = np.array([
    [ col_bg[2], col_bg[2], col_bg[2], col_bg[2],  col_bg[2]],
    [col_bg[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_bg[2], col_tar[2], col_tar[2], col_tar[2], col_bg[2]]
], dtype=np.uint8)

letra = np.stack((letra_r_u, letra_g_u, letra_b_u), axis=2)


plt.imshow(letra)
plt.show()