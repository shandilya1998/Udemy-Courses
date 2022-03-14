import cv2
import matplotlib.pyplot as plt
import numpy as np

# Opening images using OpenCV
import cv2 
image = cv2.cvtColor(
    cv2.imread('data/00-puppy.jpg'),
    cv2.COLOR_BGR2RGB
)
assert not isinstance(image, type(None))
# OpenCV does not throw an error when the image at the path does not exist
plt.imshow(image)
plt.show()
## Note that OpenCV uses BGR color model by default
## instead of a RGB color model

## The flag passed to cv2.imread(**kwargs) determines how the image is read
gray = cv2.imread('data/00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(gray, cmap = 'gray')
plt.show()

# Resize Images
n_image = cv2.resize(image, (1000, 400))
plt.imshow(n_image)
plt.show()
## The axes used the opencv methods is the opposite of the same used with numpy arrays
w_ratio = 0.5
h_ratio = 0.5
n_image = cv2.resize(image, (0, 0), image, w_ratio, h_ratio)
plt.imshow(n_image)
plt.show()

# Flip
## Vertical Axis
n_image = cv2.flip(image, 0)
plt.imshow(n_image)
plt.show()

## Horizontal Axis
n_image = cv2.flip(image, 1)
plt.imshow(n_image)
plt.show()

# Writing Images
cv2.imwrite('data/00-puppy_flipped.jpg', cv2.cvtColor(n_image, cv2.COLOR_BGR2RGB))
