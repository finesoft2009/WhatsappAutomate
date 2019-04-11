import ctypes
import numpy as np
import cv2

image = cv2.imread('img.jpg')
y=179
x=0
h=72
w=410
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
cv2.imwrite('Image.jpg', crop)
cv2.waitKey(0)

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)
