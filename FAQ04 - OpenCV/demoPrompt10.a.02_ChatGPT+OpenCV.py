# Import the necessary packages
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog
import cv2

def select_image():
    # Grab a reference to the image panels
    global panelA, panelB
    # Open a file chooser dialog and allow the user to select an input image
    path = tkinter.filedialog.askopenfilename()

	# Ensure a file path was selected
    if len(path) > 0:
        # Load the image from disk, convert it to grayscale, and detect edges in it
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 100)
        # OpenCV represents images in BGR order; however PIL represents images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Convert the images to PIL format
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)
        # and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)

        # If the panels are None, initialize them
        if panelA is None or panelB is None:
            # The first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)
            # While the second panel will store the edge map
            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)
        # Otherwise, update the image panels
        else:
            # Update the panels
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged

# Initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
# Create a button, then when pressed, will trigger a file chooser dialog and allow the user to select an input image; then add the button to the GUI
btn = Button(root, text="Select an image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# Kick off the GUI
root.mainloop()