import numpy as np
import imageio.v3 as i
import matplotlib.pyplot as plt

img = i.imread("C:\\Users\\LEN\\Documents\\Sem5\\PCD\\tami.jfif")

def zoom_out(img, factor):
    he, wd = img.shape[:2]
    nh = int(he / factor)
    nw = int(wd / factor)
    zoomed_out = np.zeros((nh, nw, 3), dtype=img.dtype)

    for y in range(nh):
        for x in range(nw):
            oriy = int(y * factor)
            orix = int(x * factor)

            oriy = min(oriy, he - 1)
            orix = min(orix, wd - 1)

            zoomed_out[y, x] = img[oriy, orix]
    
    return zoomed_out

skala = 2.0

zoomed_out_image = zoom_out(img, skala)
i.imwrite("C:\\Users\\LEN\\Documents\\Sem5\\PCD\\min.jpg", zoomed_out_image)

plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(zoomed_out_image)

plt.show()
