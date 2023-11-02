import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()  # Open a file dialog to select an image
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected

# Create the main Tkinter window
root = tk.Tk()
root.title("Image Viewer")

# Create an "Open Image" button
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Create a Label to display the image
image_label = tk.Label(root)
image_label.pack()

# Run the Tkinter main loop
root.mainloop()
