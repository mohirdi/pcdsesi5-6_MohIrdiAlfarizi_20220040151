import numpy as np
import imageio.v3 as i
import matplotlib.pyplot as plt
img =i.imread("C:\\Users\\LEN\\Documents\\Sem5\\PCD\\tami.jfif")

def zoomp(img, factor):
    he, wd =img.shape[:2]
    nh = int(he/factor)
    nw = int(wd/factor)
    izoom = np.zeros((nh,nw,3),dtype=img.dtype)

    for y in range(nh):
        for x in range(nw):

            oriy=int(y*factor)
            orix=int(x*factor)

            oriy = min(oriy, he -1)
            orix = min(orix, wd -1)

            izoom[y,x]= img[oriy, orix]
    return izoom

skala =2.0

izoom =zoomp(img, skala)
i.imwrite("C:\\Users\\LEN\\Documents\\Sem5\\PCD\\z.jpg", izoom)

plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(izoom)
plt.show()
