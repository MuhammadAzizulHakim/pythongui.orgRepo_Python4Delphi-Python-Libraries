import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

root = tk.Tk()

# Create a 2D array (e.g., grayscale image)
array = np.ones((400, 400)) * 150

# Convert the NumPy array to a PIL Image object
img = Image.fromarray(array)

# Create a Tkinter PhotoImage object from the PIL Image
tk_img = ImageTk.PhotoImage(image=img)

# Create a Tkinter Label widget and add the PhotoImage to it
label = tk.Label(root, image=tk_img)
label.pack()

root.mainloop()
