import sys
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('camera open failed')
    sys.exit()

while True:
    ret, frame = cap.read()   # bool, img

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) == 27:   # ESC to break
        break


cap.release()   # quit camera
cv2.destroyAllWindows()




