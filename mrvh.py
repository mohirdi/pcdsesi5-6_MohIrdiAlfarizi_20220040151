import numpy as np
import imageio.v3 as i
import matplotlib.pyplot as plt

img = i.imread("C:\\Users\\LEN\\Documents\\Sem5\\PCD\\tami.jfif")

he, wd = img.shape[:2]

hor_ver = np.zeros_like(img)

for y in range(he):
    for x in range(wd):
        hor_ver[y, x] = img[he - 1 - y, wd - 1 - x]

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(hor_ver)

plt.show()
