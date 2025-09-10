import numpy as np
import matplotlib.pyplot as plt

col_tar = (255, 255, 255)
col_bg = (0, 0, 0)

letra_r = np.array([[col_bg[0], col_bg[0], col_bg[0],col_bg[0], col_bg[0], col_bg[0],col_bg[0]],
                    [col_bg[0], col_tar[0], col_bg[0],col_bg[0], col_bg[0], col_tar[0],col_bg[0]],
                    [col_bg[0], col_tar[0], col_bg[0],col_bg[0], col_bg[0], col_tar[0],col_bg[0]],
                    [col_bg[0], col_tar[0], col_bg[0],col_bg[0], col_bg[0], col_tar[0],col_bg[0]],
                    [col_bg[0], col_bg[0], col_tar[0],col_bg[0], col_tar[0], col_bg[0],col_bg[0]],
                    [col_bg[0], col_bg[0], col_bg[0],col_tar[0], col_bg[0], col_bg[0],col_bg[0]],
                    [col_bg[0], col_bg[0], col_bg[0],col_bg[0], col_bg[0], col_bg[0],col_bg[0]]], dtype=np.uint8)

letra_g = np.array([[col_bg[0], col_bg[0], col_bg[0],col_bg[0], col_bg[0], col_bg[0],col_bg[0]],
                    [col_bg[0], col_tar[0], col_bg[0],col_bg[0], col_bg[0], col_tar[0],col_bg[0]],
                    [col_bg[0], col_tar[0], col_bg[0],col_bg[0], col_bg[0], col_tar[0],col_bg[0]],
                    [col_bg[0], col_tar[0], col_bg[0],col_bg[0], col_bg[0], col_tar[0],col_bg[0]],
                    [col_bg[0], col_bg[0], col_tar[0],col_bg[0], col_tar[0], col_bg[0],col_bg[0]],
                    [col_bg[0], col_bg[0], col_bg[0],col_tar[0], col_bg[0], col_bg[0],col_bg[0]],
                    [col_bg[0], col_bg[0], col_bg[0],col_bg[0], col_bg[0], col_bg[0],col_bg[0]]], dtype=np.uint8)

letra_b = np.array([[col_bg[0], col_bg[0], col_bg[0],col_bg[0], col_bg[0], col_bg[0],col_bg[0]],
                    [col_bg[0], col_tar[0], col_bg[0],col_bg[0], col_bg[0], col_tar[0],col_bg[0]],
                    [col_bg[0], col_tar[0], col_bg[0],col_bg[0], col_bg[0], col_tar[0],col_bg[0]],
                    [col_bg[0], col_tar[0], col_bg[0],col_bg[0], col_bg[0], col_tar[0],col_bg[0]],
                    [col_bg[0], col_bg[0], col_tar[0],col_bg[0], col_tar[0], col_bg[0],col_bg[0]],
                    [col_bg[0], col_bg[0], col_bg[0],col_tar[0], col_bg[0], col_bg[0],col_bg[0]],
                    [col_bg[0], col_bg[0], col_bg[0],col_bg[0], col_bg[0], col_bg[0],col_bg[0]]], dtype=np.uint8)

letra = np.stack((letra_r, letra_g, letra_b), axis=2)

plt.imshow(letra)
plt.show()