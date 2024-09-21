import cv2

# Load an image from file
image = cv2.imread('C:/Users/ASUS/bicycle-001.jpg')

# Display the image in a window
cv2.imshow('Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
