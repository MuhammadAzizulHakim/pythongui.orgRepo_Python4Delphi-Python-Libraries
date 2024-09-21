import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Create a Tkinter window
window = tk.Tk()
window.title("OpenCV with Tkinter")

# Load an image using OpenCV
cv_img = cv2.cvtColor(cv2.imread("C:/Users/ASUS/OpenCV+ChatGPT/komodo-001.jpg"), cv2.COLOR_BGR2RGB)

# Get the image dimensions
height, width, _ = cv_img.shape

# Create a canvas to display the image
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()

# Convert the NumPy ndarray to a PhotoImage
photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img))

# Add the PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# Run the Tkinter event loop
window.mainloop()
