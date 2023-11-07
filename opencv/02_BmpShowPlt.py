import matplotlib.pyplot as plt
import cv2

# show color image
# NOTE: matplotlib uses RGB, while cv2 uses BGR --> requires conversion.
imgRGB = cv2.imread('cat.bmp')
# plt.axis('off')
# plt.imshow(cv2.cvtColor(imgRGB, cv2.COLOR_BGR2RGB))
# plt.show()

# show grayscale image
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
# plt.axis('off')
# plt.imshow(imgGray, cmap='gray')
# plt.show()

# show both color and grayscale images
plt.subplot(121)
plt.axis('off')
plt.imshow(cv2.cvtColor(imgRGB, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()
