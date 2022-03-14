import numpy as np
import matplotlib.pyplot as plt

# Opening images using PIL
from PIL import Image
image = Image.open('data/00-puppy.jpg')
## PIL does not directly output NumPy Arrays
image = np.asarray(image)
plt.imshow(image)
plt.show()

# Plot Red Channel
## Channel Last Representation is used by default 
## in both PIL and OpenCV
plt.imshow(image[:, :, 0], cmap = 'gray')
plt.show()
