import cv2
import numpy as np

img_m = cv2.imread('model.jpg')
hsv_m = cv2.cvtColor(img_m, cv2.COLOR_BGR2HSV)
hist_m = cv2.calcHist([hsv_m], [0, 1], None, [180, 256], [0, 180, 0, 256])

img_i = cv2.imread('hand.jpg')
hsv_i = cv2.cvtColor(img_i, cv2.COLOR_BGR2HSV);
hist_i = cv2.calcHist([hsv_i], [0, 1], None, [180, 256], [0, 180, 0, 256])

hist_m /= np.size(hsv_m)
hist_i /= np.size(hsv_i)

print("maximum of hist_m : %f" % hist_m.max())
print("maximum of hist_i : %f" % hist_i.max())

hist_r = np.divide(hist_m,(hist_i+1e-7))
hist_r = np.minimum(hist_r, 1.0)
print("range of hist_r: [%.1f, %.1f]"%(hist_r.min(), hist_r.max()))

result = np.zeros(img_i.shape)
height, width = img_i.shape[0], img_i.shape[1]
h,s,v = cv2.split(hsv_i)

for i in range(height):
    for j in range(width):
        h_value = h[i,j]
        s_value = s[i,j]
        result[i,j] = hist_r[h_value, s_value]

ret, thresholded = cv2.threshold(result, 0.02, 255, cv2.THRESH_BINARY)
cv2.imwrite('result.jpg', thresholded)

kernel =  np.ones((3,3))
morphology = cv2.morphologyEx(thresholded,cv2.MORPH_CLOSE,kernel, iterations=6)

cv2.imwrite('morphology.jpg', morphology)