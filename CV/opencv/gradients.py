import numpy as np
import cv2
import matplotlib.pyplot as plt

def display(img):
    plt.imshow(img, cmap = 'gray')
    plt.show()

img = cv2.imread('data/sudoku.jpg', 0)
display(img)

sobel_x = cv2.Sobel(img, ddepth = cv2.CV_64F, dx = 1, dy = 0, ksize = 5)
#display(sobel_x)

sobel_y = cv2.Sobel(img, ddepth = cv2.CV_64F, dx = 0, dy = 1, ksize = 5)
#display(sobel_y)

# Laplacian Derivative
laplacian = cv2.Laplacian(img, ddepth = cv2.CV_64F)
#display(laplacian)

blended = cv2.addWeighted(src1 = sobel_x, alpha = 0.5, src2 = sobel_y, beta = 0.5, gamma = 0)
display(blended)

ret, thresh1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
#display(thresh1)

ret, thresh2 = cv2.threshold(blended, 100, 200, cv2.THRESH_BINARY)
#display(thresh2)

kernel = np.ones((4, 4), dtype = np.uint8)
gradient = cv2.morphologyEx(blended, cv2.MORPH_GRADIENT, kernel)
display(gradient)
