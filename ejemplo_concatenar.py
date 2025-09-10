import numpy as np
import matplotlib.pyplot as plt

col_tar = (0, 0, 255)  
col_bg = (0, 128, 0)   

letra_r_h = np.array([
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_tar[0], col_tar[0], col_tar[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]]
], dtype=np.uint8)

letra_g_h = np.array([
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_tar[1], col_tar[1], col_tar[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]]
], dtype=np.uint8)

letra_b_h = np.array([
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_tar[2], col_tar[2], col_tar[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]]
], dtype=np.uint8)

letra_h = np.stack((letra_r_h, letra_g_h, letra_b_h), axis=2)


col_tar = (0, 0, 128)   
col_bg  = (230, 240, 255) 

letra_r = np.array([[col_bg[1],  col_bg[1], col_bg[1], col_bg[1]], 
                    [col_bg[1], col_bg[1], col_bg[1], col_bg[1]], 
                    [col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
                    [col_bg[1], col_tar[2], col_tar[2], col_bg[1]],
                    [col_tar[2], col_bg[1], col_bg[1], col_tar[2]],
                    [col_tar[2], col_bg[1], col_bg[1], col_tar[2]], 
                    [col_bg[1], col_tar[2], col_tar[2], col_bg[1]]], dtype=np.uint8)

letra_g = np.array([[col_bg[2],  col_bg[2], col_bg[2], col_bg[2]], 
                    [col_bg[2], col_bg[2], col_bg[2], col_bg[2]], 
                    [col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
                    [col_bg[2], col_tar[0], col_tar[0], col_bg[2]],
                    [col_tar[0], col_bg[2], col_bg[2], col_tar[0]],
                    [col_tar[0], col_bg[2], col_bg[2], col_tar[0]], 
                    [col_bg[2], col_tar[0], col_tar[0], col_bg[2]]], dtype=np.uint8)


letra_b = np.array([[col_bg[2],  col_bg[2], col_bg[2], col_bg[2]], 
                    [col_bg[2], col_bg[2], col_bg[2], col_bg[2]], 
                    [col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
                    [col_bg[2], col_tar[1], col_tar[1], col_bg[2]],
                    [col_tar[1], col_bg[2], col_bg[2], col_tar[1]],
                    [col_tar[1], col_bg[2], col_bg[2], col_tar[1]], 
                    [col_bg[2], col_tar[0], col_tar[0], col_bg[2]]], dtype=np.uint8)

letra_o = np.stack((letra_r, letra_g, letra_b), axis=2)
letras_ho = np.concatenate((letra_h, letra_o), axis=1)


from PIL import Image
img = Image.fromarray(letras_ho, 'RGB')
img.save('letras_ho.png')

print(img.size)
img_resized = img.resize((700, 900))
img_resized.save('letras_ho_resized.png')

letras_ho_resized = np.array(img_resized)

print(letras_ho_resized.shape)


