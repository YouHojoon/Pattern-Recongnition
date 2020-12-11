import cv2
import time

img = cv2.imread('butterfly.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
surf = cv2.xfeatures2d.SURF_create()

start = time.time()
sift.detect(image=gray, mask=None)
end = time.time()
sift_perform = end - start

start = time.time()
surf.detect(image=gray, mask=None)
end = time.time()
surf_perform = end - start

print(gray.shape)
print("SIFT : ",sift_perform)
print("SURF : ",surf_perform)

gray = cv2.resize(gray,None,fx=2.0,fy=2.0)

start = time.time()
sift.detect(image=gray, mask=None)
end = time.time()
sift_perform = end - start

start = time.time()
surf.detect(image=gray, mask=None)
end = time.time()
surf_perform = end - start

print(gray.shape)
print("SIFT : ",sift_perform)
print("SURF : ",surf_perform)

gray = cv2.resize(gray,None,fx=2.0,fy=2.0)

start = time.time()
sift.detect(image=gray, mask=None)
end = time.time()
sift_perform = end - start

start = time.time()
surf.detect(image=gray, mask=None)
end = time.time()
surf_perform = end - start

print(gray.shape)
print("SIFT : ",sift_perform)
print("SURF : ",surf_perform)