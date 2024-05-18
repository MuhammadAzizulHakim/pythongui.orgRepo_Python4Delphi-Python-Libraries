# Import the necessary packages
import imutils
import cv2
import argparse

# Load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("C:/Users/ASUS/got.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)