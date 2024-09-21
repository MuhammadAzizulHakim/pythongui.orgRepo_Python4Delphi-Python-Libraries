import cv2

# Read image in grayscale
img_grayscale = cv2.imread('C:/Users/ASUS/bruce-lee-1972.jpg', 0)

# Display the image in a window
cv2.imshow('grayscale image', img_grayscale)
cv2.waitKey(0)

# Save the image to a file
cv2.imwrite('C:/Users/ASUS/OpenCV-Demos/bruce-lee-1972_grayscale.jpg', img_grayscale)