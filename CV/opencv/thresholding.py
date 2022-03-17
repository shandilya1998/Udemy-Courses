import numpy as np
import cv2
import matplotlib.pyplot as plt

"""
    Refer to the following link for cv2::ThresholdTypes
    https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#gaa9e58d2860d4afa658ef70a9b1115576
"""

# Reading the image in grayscale
img = cv2.imread('data/rainbow.jpg', 0)
plt.imshow(img, cmap = 'gray')
plt.show()

# Thresholding
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap = 'gray')
plt.show()

# Inverse Thresholding
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
plt.imshow(thresh2, cmap = 'gray')
plt.show()

# Threshold Truncation
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
plt.imshow(thresh3, cmap = 'gray')
plt.show()

# Threshold To Zero
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
plt.imshow(thresh4, cmap = 'gray')
plt.show()

# Threshold To Zero Inverse
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
plt.imshow(thresh5, cmap = 'gray')
plt.show()

# Application of Thresholding
img = cv2.imread('data/crossword.jpg', 0)
def show(img):
    fig, ax = plt.subplots(1, 1, figsize = (15, 15))
    ax.imshow(img, cmap = 'gray')
    plt.show()

show(img)

# Binary Threshold
ret, thresh6 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
show(thresh6)

# Adaptive Threshodl
thresh7 = cv2.adaptiveThreshold(
    img,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    15,
    8
)
show(thresh7)
