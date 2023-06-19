import cv2
import numpy as np
import random


def encrypt():
    random.seed(10)
    img1 = cv2.imread('pic1.jpg')
    img2 = cv2.imread('pic2.jpg')
    garyimage = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(garyimage, 127, 255, cv2.THRESH_BINARY)
    for i in range(blackAndWhiteImage.shape[0]):
        for j in range(blackAndWhiteImage.shape[1]):
            x, y, z = int(random.random()*100000), int(random.random()*100000), int(random.random()*100000)

            xx , yy  , zz = img1.shape
            x %= xx
            y %= yy
            z %= zz
            if blackAndWhiteImage[i][j] % 2 == 0:
                if img1[x][y][z] % 2 == 1:
                    img1[x][y][z] -= 1
            else:
                if img1[x][y][z] % 2 == 0:
                    img1[x][y][z] += 1
    cv2.imshow('encrypted' , img1)
    cv2.waitKey(0)
    cv2.imwrite("encrypted.png" , img1)


def decrypt():
    random.seed(10)
    encrypted = cv2.imread("encrypted.png")
    image = cv2.imread("pic2.jpg")
    xx , yy , zz = image.shape
    xxx,yyy,zzz=encrypted.shape
    decrypted = np.zeros((xx , yy) , dtype=np.uint8)
    for i in range(xx):
        for j in range(yy):
            x, y, z = int(random.random()*100000), int(random.random()*100000), int(random.random()*100000)
            x %= xxx
            y %= yyy
            z %= 3
            if encrypted[x][y][z] % 2 == 1:
                decrypted[i][j] = 255
    cv2.imshow('decrypted' , decrypted)
    cv2.waitKey(0)
    cv2.imwrite("decrypted.png" , decrypted)



encrypt()
decrypt()
