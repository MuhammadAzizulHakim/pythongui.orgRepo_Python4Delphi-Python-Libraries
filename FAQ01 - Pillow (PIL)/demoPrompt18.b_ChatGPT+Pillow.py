import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog

class MyGui:
    def __init__(self, root):
        self.root = root
        self.root.title("PAGE GUI with Pillow")

        # Create a Tkinter image widget
        self.image_label = ttk.Label(root)
        self.image_label.grid(row=0, column=0, padx=10, pady=10)

        # Create a button to open an image
        open_button = ttk.Button(root, text="Open Image", command=self.open_image)
        open_button.grid(row=1, column=0, padx=10, pady=10)

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff")])

        if file_path:
            # Open and display the image using Pillow
            pil_image = Image.open(file_path)
            tk_image = ImageTk.PhotoImage(pil_image)

            # Update the Tkinter image widget
            self.image_label.configure(image=tk_image)
            self.image_label.image = tk_image  # Keep a reference to prevent garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = MyGui(root)
    root.mainloop()
