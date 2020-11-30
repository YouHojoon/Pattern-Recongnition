import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(17, 5))

img = cv2.imread('hand.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height = img.shape[0]
width = img.shape[1]
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.axis('off')
plt.title('original')


# OpenCV를 이용한 변환 행렬 도출
center = (width / 2, height / 2)
cv_M = cv2.getRotationMatrix2D(center, 90, 1.0)  # 회전 방향이 반시계방향(CCW; Counter Clock-Wise)
cv_result = cv2.warpAffine(img, cv_M, (width, height))
print('>> OpenCV Rotation matrix')
print(cv_M, end='\n\n')

plt.subplot(1, 3, 2)
plt.imshow(cv_result)
plt.axis('off')
plt.title('cv_result')

theta = np.deg2rad(90)
my_m = np.array([[1,0,-width/2],[0,1,-height/2],[0,0,1]])
my_m = np.array([[np.cos(theta),np.sin(theta),1],[-np.sin(theta),np.cos(theta),1],[0,0,1]]).dot(my_m)
my_m = np.array([[1,0,width/2],[0,1,height/2],[0,0,1]]).dot(my_m)

print('>> My matrix')
print(my_m[:2])
my_result = cv2.warpAffine(img, my_m[:2], (width, height))

plt.subplot(1, 3, 3)
plt.imshow(my_result)
plt.axis('off')
plt.title('my_result')

# figure 출력
plt.tight_layout()
plt.show()
