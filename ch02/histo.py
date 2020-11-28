import cv2
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist(gray_img,[0],None,[256],[0,256])



print(hist.reshape(-1))
plt.plot(hist)
plt.show()
cv2.imshow('image',gray_img)
cv2.waitKey()