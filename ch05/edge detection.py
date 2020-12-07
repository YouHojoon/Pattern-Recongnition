import cv2



cap = cv2.VideoCapture('./test_videos/challenge.mp4')
def pipe(image):
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, (15, 15), 0.0)
    edg_img = cv2.Canny(blurred_img, 50, 150)

    return edg_img

while True:
    ok, frame = cap.read()

    if not ok:
        break;

    edg_img=pipe(frame)
    cv2.imshow('edge',edg_img)
    key=cv2.waitKey(30)
    if key == ord('x'):
        break;
