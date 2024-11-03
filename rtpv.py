import numpy as np
import imageio.v3 as i
import matplotlib.pyplot as plt

img = i.imread("C:\\Users\\LEN\\Documents\\Sem5\\PCD\\tami.jfif")

def rot(img, deg):
    radeg = np.radians(deg)
    cosdeg, sindeg = np.cos(radeg), np.sin(radeg)

    he, wd = img.shape[:2]
    max_dim = int(np.sqrt(he**2 + wd**2))
    outp = np.zeros((max_dim, max_dim, 3), dtype=img.dtype)

    for y in range(he):
        for x in range(wd):
            newx = int(cosdeg * x - sindeg * y)
            newy = int(sindeg * x + cosdeg * y)

            if 0 <= newx < max_dim and 0 <= newy < max_dim:
                outp[newy, newx] = img[y, x]

    return outp

rotI = rot(img, 45)

plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(rotI)

plt.show()
