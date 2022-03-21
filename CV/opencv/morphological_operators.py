import numpy as np
import cv2
import matplotlib.pyplot as plt

def load():
    blank_img =np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300), fontFace=font,fontScale= 5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
    return blank_img

def display(img):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

img = load()
display(img)

"""
    Morphological Operators are specialised kernels
    aimed at specific effects
"""

# Erosion
kernel = np.ones((5, 5), dtype = np.uint8)
dst = cv2.erode(img, kernel, iterations = 4)
#display(dst)

# Opening
## Erosion followed by Dilation
## Meant to remove noise from image
## Good for removing noise from the background
noise = np.random.randint(low = 0, high = 2, size = img.shape) * 255
n_img = (img + noise) / 2
#display(n_img)
dst = cv2.morphologyEx(n_img, cv2.MORPH_OPEN, kernel)
#display(dst)

# Closing
## Dilation followed by Erosion
## Good for removing noide from the foreground
black_noise = noise * -1
n_img = img + black_noise
n_img[n_img == -255] = 0
#display(n_img)
dst = cv2.morphologyEx(n_img, cv2.MORPH_CLOSE, kernel)
#display(dst)

# Morphological Gradient
## Takes the difference between Dilation and Erosion of an image
## A very simple method of edge detection
dst = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
display(dst)
