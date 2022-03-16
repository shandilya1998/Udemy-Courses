import numpy as np
import cv2
import matplotlib.pyplot as plt

bgr_image = cv2.imread('data/00-puppy.jpg')
plt.imshow(bgr_image)
plt.show()

rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.show()
hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
plt.imshow(hsv_image)
plt.show()

# Plotting HSV images in matplotlib
from matplotlib.colors import hsv_to_rgb
plt.imshow(cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB))
plt.show()
