import numpy as np
import imageio.v3 as i
import matplotlib.pyplot as plt
img =i.imread("C:\\Users\\LEN\\Documents\\Sem5\\PCD\\tami.jfif")

def rot(img,deg):
    radeg = np.radians(deg)
    cosdeg,sindeg= np.cos(radeg), np.sin(radeg)

    he,wd = img.shape[:2]
    max= int(np.sqrt(he**2 +wd**2 ))
    outp = np.zeros((max,max,3),dtype=img.dtype)

    cy, cx = max//2, max//2

    for y in range(-he//2, he//2):
        for x in range(-wd//2, wd//2):
            newx = int(cosdeg* x-sindeg*y)+cx
            newy = int(sindeg* x+cosdeg*y)+cy

            if 0<= newx < max and 0<= newy <max:
                outp[newy,newx] = img[y+he//2, x+wd//2]
        return outp
rotI = rot(img, 45)

plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(rotI)

plt.show()