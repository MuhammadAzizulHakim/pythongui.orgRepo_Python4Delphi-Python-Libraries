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

# Display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)