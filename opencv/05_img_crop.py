import numpy as np
import cv2

'''
img1 = cv2.imread('HappyFish.jpg')
img2 = img1[40:120, 30:150]   # crop image
img3 = img1[40:120, 30:150].copy()  # crop image to deep copy

img2.fill(0)  # fill black

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
'''

img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
img_face = img[200:400, 200:400]   # crop face
cv2.add(img_face, 50, img_face)   # make face brighter
cv2.circle(img_face, (100,100), 80, 0, 2)   # circle face: center, radius, color, thickness

cv2.imshow('img', img)
cv2.imshow('img_face', img_face)
cv2.waitKey()
