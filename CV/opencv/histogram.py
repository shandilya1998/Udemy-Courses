import numpy as np
import cv2
import matplotlib.pyplot as plt

dark_horse = cv2.imread('data/horse.jpg')
show_horse = cv2.cvtColor(dark_horse, cv2.COLOR_BGR2RGB)

rainbow = cv2.imread('data/rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread('data/bricks.jpg')
show_bricks = cv2.cvtColor(blue_bricks, cv2.COLOR_BGR2RGB)

"""
plt.imshow(show_horse)
plt.show()

plt.imshow(show_rainbow)
plt.show()

plt.imshow(show_bricks)
plt.show()
"""

fig, ax = plt.subplots(3, 3, figsize = (12, 12))
colors = ['b', 'g', 'r']

ax[1][0].set_xlim([0, 256])
ax[1][1].set_xlim([0, 256])
ax[1][2].set_xlim([0, 256])
ax[1][1].set_ylim([0, int(5e5)])

ax[0][0].imshow(show_bricks)
ax[0][1].imshow(show_horse)
ax[0][2].imshow(show_rainbow)

ax[0][0].set_title('Blue Bricks')
ax[0][1].set_title('Dark Horse')
ax[0][2].set_title('Rainbow')

for i, color in enumerate(colors):
    
    mask = np.zeros(blue_bricks.shape[:2], dtype = np.uint8)
    mask[
        mask.shape[0] // 4: 3 * mask.shape[0] // 4,
        mask.shape[1] // 4: 3 * mask.shape[1] // 4
    ] = 255
    hist_bricks = cv2.calcHist(
        [blue_bricks],
        channels = [i],
        mask = None,
        histSize = [256],
        ranges = [0, 256]
    )
    masked_hist_bricks = cv2.calcHist(
        [blue_bricks],
        channels = [i],
        mask = mask,
        histSize = [256],
        ranges = [0, 256]
    )

    mask = np.zeros(dark_horse.shape[:2], dtype = np.uint8)
    mask[
        4 * mask.shape[0] // 10: 6 * mask.shape[0] // 10,
        4 * mask.shape[1] // 10: 6 * mask.shape[1] // 10
    ] = 255
    hist_horse = cv2.calcHist(
        [dark_horse],
        channels = [i],
        mask = None,
        histSize = [256],
        ranges = [0, 256]
    )
    masked_hist_horse = cv2.calcHist(
        [dark_horse],
        channels = [i],
        mask = mask,
        histSize = [256],
        ranges = [0, 256]
    )

    mask = np.zeros(rainbow.shape[:2], dtype = np.uint8)
    mask[
        mask.shape[0] // 4: 3 * mask.shape[0] // 4,
        mask.shape[1] // 4: 3 * mask.shape[1] // 4
    ] = 255
    hist_rainbow = cv2.calcHist(
        [rainbow],
        channels = [i],
        mask = None,
        histSize = [256],
        ranges = [0, 256]
    )
    masked_hist_rainbow = cv2.calcHist(
        [rainbow],
        channels = [i],
        mask = mask,
        histSize = [256],
        ranges = [0, 256]
    )

    ax[1][0].plot(hist_bricks, color = color)
    ax[2][0].plot(masked_hist_bricks, color = color)
    ax[1][1].plot(hist_horse, color = color)
    ax[2][1].plot(masked_hist_horse, color = color)
    ax[1][2].plot(hist_rainbow, color = color)
    ax[2][2].plot(masked_hist_rainbow, color = color)

ax[1][0].set_title('Blue Bricks Histogram')
ax[2][0].set_title('Masked Blue Bricks Histogram')
ax[1][1].set_title('Dark Horse Histogram')
ax[2][1].set_title('Masked Dark Horse Histogram')
ax[1][2].set_title('Rainbow Histogram')
ax[2][2].set_title('Masked Rainbow Histogram')

fig.tight_layout()

img = cv2.imread('data/gorilla.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fig, ax = plt.subplots(2, 2, figsize = (5, 5))
hist_values = cv2.calcHist(
    [gray_img],
    channels = [0],
    mask = None,
    histSize = [256],
    ranges = [0, 256]
)

eq_img = cv2.equalizeHist(gray_img)
eq_hist = cv2.calcHist(
    [eq_img],
    channels = [0],
    mask = None,
    histSize = [256],
    ranges = [0, 256]
)

ax[0][0].imshow(gray_img, cmap = 'gray')
ax[0][0].set_title('Grayscale Gorilla')
ax[1][0].plot(hist_values)
ax[1][0].set_title('Histogram')
ax[0][1].imshow(eq_img, cmap = 'gray')
ax[0][1].set_title('Histogram Normalised Gorilla')
ax[1][1].plot(eq_hist)
ax[1][1].set_title('Normalised Histogram')
fig.tight_layout()

fig, ax = plt.subplots(2, 2, figsize = (5, 5)) 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hist_values = cv2.calcHist(
    [hsv],
    channels = [2],
    mask = None,
    histSize = [256],
    ranges = [0, 256]
)

eq_hsv = hsv.copy()
eq_hsv[:, :, 2] = cv2.equalizeHist(eq_hsv[:, :, 2 ])
eq_rgb = cv2.cvtColor(eq_hsv, cv2.COLOR_HSV2RGB)
eq_hist = cv2.calcHist(
    [eq_hsv],
    channels = [2],
    mask = None,
    histSize = [256],
    ranges = [0, 256]
)

ax[0][0].imshow(rgb)
ax[0][0].set_title('Gorilla')
ax[1][0].plot(hist_values)
ax[1][0].set_title('Histogram')
ax[0][1].imshow(eq_rgb)
ax[0][1].set_title('Histogram Normalised Gorilla')
ax[1][1].plot(eq_hist)
ax[1][1].set_title('Normalised Histogram')
fig.tight_layout()

plt.show()
