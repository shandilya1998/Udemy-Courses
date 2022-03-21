import numpy as np
import cv2
import matplotlib.pyplot as plt

# Utility Functions
## Load Image
def load_test_image():
    img = cv2.imread('data/bricks.jpg').astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def display(img):
    fig, ax = plt.subplots(1, 1, figsize = (12, 10))
    ax.imshow(img)
    plt.show()

img = load_test_image()
#display(img)

# Gamma Correction
## Practical Effect increases or decreases the brighness of the image
## The range of values within the image must be [0, 1]
## Values less than 1 increase image brightness
## Values more than 1 decrease image brightness
gamma = 1 / 4
result = np.power(img, gamma)
#display(result)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = 'BRICKS', org = (10, 600), fontFace = font, fontScale = 10, color = (255, 0, 0), thickness = 4)
#display(img)

# Blurring with 2D convolution using Low Pass Filter
## Larger the kernel greater the blurring
## Sum of all kernel values must be one
kernel = np.ones((9, 9), dtype = np.float32) / 81
dst = cv2.filter2D(img, ddepth = -1, kernel = kernel)
#display(dst)

# CV2 Default Blurring Kernel
dst = cv2.blur(img, ksize = (9, 9))
#display(dst)

# Gaussian Blurring
## sigmaY, if not assigned, is equal to sigmaX
dst = cv2.GaussianBlur(img, ksize = (9, 9), sigmaX = 10, sigmaY = 10)
#display(dst)

# Median Blurring
## Good for removing noise while keeping details in check
dst = cv2.medianBlur(img, 5)
#display(dst)

img = cv2.cvtColor(cv2.imread('data/sammy.jpg'), cv2.COLOR_BGR2RGB)
#display(img)

n_img = cv2.cvtColor(cv2.imread('data/sammy_noise.jpg'), cv2.COLOR_BGR2RGB)
#display(n_img)

dst = cv2.medianBlur(n_img, 5)
#display(dst)

img = load_test_image()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text = 'BRICKS', org = (10, 600), fontFace = font, fontScale = 10, color = (255, 0, 0), thickness = 4)
dst = cv2.bilateralFilter(img, 9, 75, 75)
display(img)
display(dst)
