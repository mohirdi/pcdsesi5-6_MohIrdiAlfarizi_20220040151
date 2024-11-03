import numpy as np
import imageio.v3 as i
import matplotlib.pyplot as plt
img =i.imread("C:\\Users\\LEN\\Documents\\Sem5\\PCD\\tami.jfif")

def Translasi (img,shiftX,shiftY):
    itr = np.roll(img, shift=shiftY, axis=0)
    itr = np.roll(itr, shift=shiftX, axis=1)

    if shiftY >0:
        itr[shiftY, :]=0
    elif shiftY<0:
        itr[shiftY, :]=0
    if shiftX >0:
        itr[shiftX, :]=0
    elif shiftX<0:
        itr[shiftX, :]=0

    return itr

iResult = Translasi(img,shiftX=50,shiftY=-100)

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.imshow(img)
plt.subplot(2,1,2)
plt.imshow(iResult)
plt.show()