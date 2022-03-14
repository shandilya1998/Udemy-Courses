import numpy as np
import cv2
import matplotlib.pyplot as plt

image = np.zeros((512, 512, 3), dtype = np.uint8)
plt.imshow(image)
plt.show()

# Rectangle
## pt1 --> Top Left Corner
## pt2 ->> Bottom Right Corner
## Notice the second coordinate is the y-axis and the first axis is the x axis
## In Numpy the first coordinate is the column number whereas the second coordinate is the row number.
## Thus,
## row --> x-axis
## column --> y-axis
n_image = image.copy()
cv2.rectangle(n_image, pt1 = (284, 80), pt2 = (410, 250), color = (255, 255, 0), thickness = 10)
plt.imshow(n_image)
plt.show()

# Circle
cv2.circle(n_image, center = (100, 100), radius = 50, color = (255, 0, 255), thickness = 5)
plt.imshow(n_image)
plt.show()

# Filled Figure
cv2.circle(n_image, center = (300, 300), radius = 50, color = (255, 255, 255), thickness = -1)
plt.imshow(n_image)
plt.show()

# Line
cv2.line(n_image, pt1 = (0, 0), pt2 = (512, 512), color = (123, 142, 234), thickness = 2)
plt.imshow(n_image)
plt.show()

# Text
font = cv2.FONT_HERSHEY_SIMPLEX
# org is the bottom left corner of the text box
cv2.putText(
    n_image,
    text = 'Hello! World',
    org = (10, 500),
    fontFace = font,
    fontScale = 1,
    color = (155, 155, 155),
    thickness = 3,
    lineType = cv2.LINE_AA
)
plt.imshow(n_image)
plt.show()

# Polygon
n_image = image.copy()
vertices = np.array([[100, 300], [200, 200], [400, 300], [200, 400]], dtype = np.int32)
pts = vertices.reshape((-1, 1, 2))
cv2.polylines(n_image, [pts], isClosed = True, color = (0, 0, 255), thickness = 5)
plt.imshow(n_image)
plt.show()
