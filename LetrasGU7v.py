import numpy as np
import matplotlib.pyplot as plt

col_tar = (0, 0, 0)  # Negro
col_bg = (255, 255, 255) # Blanco

# --- Letra G  ---

letraG_r = np.array([
    [col_bg[0], col_tar[0], col_tar[0], col_tar[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_tar[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_bg[0], col_tar[0], col_tar[0], col_tar[0], col_tar[0]]
], dtype=np.uint8)


letraG_g = np.array([
    [col_bg[1], col_tar[1], col_tar[1], col_tar[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_tar[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_bg[1], col_tar[1], col_tar[1], col_tar[1], col_tar[1]]
], dtype=np.uint8)


letraG_b = np.array([
    [col_bg[2], col_tar[2], col_tar[2], col_tar[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_tar[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_bg[2], col_tar[2], col_tar[2], col_tar[2], col_tar[2]]
], dtype=np.uint8)

letraG = np.stack((letraG_r, letraG_g, letraG_b), axis=2)
plt.figure()
plt.imshow(letraG)
plt.title('Letra G')

# --- Letra U  ---

letraU_r = np.array([
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_bg[0], col_tar[0], col_tar[0], col_tar[0], col_bg[0]]
], dtype=np.uint8)


letraU_g = np.array([
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_tar[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_bg[1], col_tar[1], col_tar[1], col_tar[1], col_bg[1]]
], dtype=np.uint8)


letraU_b = np.array([
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_tar[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_bg[2], col_tar[2], col_tar[2], col_tar[2], col_bg[2]]
], dtype=np.uint8)

letraU = np.stack((letraU_r, letraU_g, letraU_b), axis=2)
plt.figure()
plt.imshow(letraU)
plt.title('Letra U')

# --- numero 7  ---

numero7_r = np.array([
    [col_tar[0], col_tar[0], col_tar[0], col_tar[0], col_tar[0]],
    [col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_bg[0], col_bg[0], col_bg[0], col_tar[0], col_bg[0]],
    [col_bg[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0]],
    [col_bg[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0]],
    [col_bg[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_bg[0], col_tar[0], col_bg[0], col_bg[0], col_bg[0]]
], dtype=np.uint8)


numero7_g = np.array([
    [col_tar[1], col_tar[1], col_tar[1], col_tar[1], col_tar[1]],
    [col_bg[1], col_bg[1], col_bg[1], col_bg[1], col_tar[1]],
    [col_bg[1], col_bg[1], col_bg[1], col_tar[1], col_bg[1]],
    [col_bg[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1]],
    [col_bg[1], col_bg[1], col_tar[1], col_bg[1], col_bg[1]],
    [col_bg[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1]],
    [col_bg[1], col_tar[1], col_bg[1], col_bg[1], col_bg[1]]
], dtype=np.uint8)


numero7_b = np.array([
    [col_tar[2], col_tar[2], col_tar[2], col_tar[2], col_tar[2]],
    [col_bg[2], col_bg[2], col_bg[2], col_bg[2], col_tar[2]],
    [col_bg[2], col_bg[2], col_bg[2], col_tar[2], col_bg[2]],
    [col_bg[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2]],
    [col_bg[2], col_bg[2], col_tar[2], col_bg[2], col_bg[2]],
    [col_bg[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2]],
    [col_bg[2], col_tar[2], col_bg[2], col_bg[2], col_bg[2]]
], dtype=np.uint8)

numero7 = np.stack((numero7_r, numero7_g, numero7_b), axis=2)
plt.figure()
plt.imshow(numero7)
plt.title('Número 7')

# --- Letra v (minúscula, con el método conciso de np.stack) ---

letrav_base = np.array([
    [col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]], 
    [col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_bg[0], col_bg[0], col_bg[0], col_bg[0], col_bg[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_tar[0], col_bg[0], col_bg[0], col_bg[0], col_tar[0]],
    [col_bg[0], col_tar[0], col_bg[0], col_tar[0], col_bg[0]],
    [col_bg[0], col_bg[0], col_tar[0], col_bg[0], col_bg[0]]
], dtype=np.uint8)

# Apilamos la matriz base tres veces para formar la imagen RGB
letrav = np.stack((letrav_base, letrav_base, letrav_base), axis=2)
plt.figure()
plt.imshow(letrav)
plt.title('Letra v (minúscula)')

# Mostrar todas las figuras
plt.show()