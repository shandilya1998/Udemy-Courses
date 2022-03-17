import numpy as np
import cv2
import matplotlib.pyplot as plt

# Blending
img1 = cv2.imread('data/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('data/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.show()

#plt.imshow(img2)
#plt.show()

r_img1 = cv2.resize(img1, (1200, 1200))
r_img2 = cv2.resize(img2, (1200, 1200))

#plt.imshow(r_img1)
#plt.show()

#plt.imshow(r_img2)
#plt.show()

# Images must be of the same size
blended = cv2.addWeighted(r_img1, 0.8, r_img2, 0.2, 0.0)
plt.imshow(blended)
plt.show()

# Overlay
r_img2 = cv2.resize(img2, (600, 600))
#plt.imshow(r_img2)
#plt.show()

large = img1.copy()
small = r_img2.copy()

x_offset = 0
y_offset = 0
x_end = x_offset + small.shape[1]
y_end = y_offset + small.shape[0]

large[x_offset: x_end, y_offset: y_end] = small

#plt.imshow(large)
#plt.show()

# Blending Images of different sizes
## Blending at the bottom right
rows, cols, channels = r_img2.shape

roi = img1[-rows:, -cols:]

g_img2 = cv2.cvtColor(r_img2, cv2.COLOR_RGB2GRAY)
plt.imshow(g_img2, cmap = 'gray')
plt.show()

# Calculating Inverse of grayscale image
mask = cv2.bitwise_not(g_img2)
plt.imshow(mask, cmap = 'gray')
plt.show()

white_background = np.full(r_img2.shape, 255, dtype = np.uint8)
bk = cv2.bitwise_or(white_background, white_background, mask = mask)
plt.imshow(bk)
plt.show()

fg = cv2.bitwise_or(r_img2, r_img2, mask = mask)

roi = cv2.bitwise_or(roi, fg)
plt.imshow(roi)
plt.show()

large = img1.copy()
small = roi

large[-roi.shape[0]:, -roi.shape[1]:] = roi
plt.imshow(large)
plt.show()
