import numpy as np
import imageio.v3 as i
import matplotlib.pyplot as plt
img =i.imread("C:\\Users\\LEN\\Documents\\Sem5\\PCD\\tami.jfif")

he, wd = img.shape[:2]
hor = np.zeros_like(img)
ver = np.zeros_like(img)


for y in range(he):
    for x in range(wd):
        hor[y,x] = img[y,wd - 1 -x ]

for y in range(he):
    for x in range(wd):
        ver[y,x] = img[he - 1 -y,x ]

plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.imshow(img)

plt.subplot(1,3,2)
plt.imshow(hor)

plt.subplot(1,3,3)
plt.imshow(ver)

plt.show()