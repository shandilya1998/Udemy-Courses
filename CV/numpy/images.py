import numpy as np
import matplotlib.pyplot as plt

# Opening images using PIL
from PIL import Image
image = Image.open('data/00-puppy.jpg')
## PIL does not directly output NumPy Arrays
image = np.asarray(image)
plt.imshow(image)
plt.show()

# Opening images using OpenCV
import cv2
image = cv2.cvtColor(
    cv2.imread('data/00-puppy.jpg'),
    cv2.COLOR_BGR2RGB
)
plt.imshow(image)
plt.show()
## Note that OpenCV uses BGR color model by default
## instead of a RGB color model

# Plot Red Channel
## Channel Last Representation is used by default 
## in both PIL and OpenCV
plt.imshow(image[:, :, 0], cmap = 'gray')
plt.show()
