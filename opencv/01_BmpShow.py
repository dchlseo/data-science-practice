import sys
import cv2

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('image load failed.')
    sys.exit()

# cv2.imwrite('cat.png', img)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)
while True:
    if cv2.waitKey() == ord('q'):
    # if cv2.waitKey() == 27  # = esc
        break

# cv2.destroyWindow('image')


