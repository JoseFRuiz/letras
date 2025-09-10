import numpy as np
import matplotlib.pyplot as plt

col_tar = (255, 0, 0)    
col_bg  = (255, 255, 255) 


letrak_r = np.array([
    [col_tar[0], col_bg[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0]]
], dtype=np.uint8)


letrak_g = np.array([
    [col_tar[1], col_bg[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1]]
], dtype=np.uint8)


letrak_b = np.array([
    [col_tar[2], col_bg[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2]]
], dtype=np.uint8)


letrak = np.stack((letrak_r, letrak_g, letrak_b), axis=2)

plt.imshow(letrak)
plt.show()



