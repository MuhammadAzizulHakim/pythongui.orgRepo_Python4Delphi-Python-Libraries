import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenCV with Tkinter")

        self.label = ttk.Label(root)
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.button = ttk.Button(root, text="Capture Image", command=self.capture_image)
        self.button.grid(row=1, column=0, padx=10, pady=10)

        self.cap = cv2.VideoCapture(0)  # Use 0 for the default camera

    def capture_image(self):
        if not self.cap.isOpened():
            print("Error: Could not open video.")
            return

        # Read one frame
        ret, frame = self.cap.read()

        if not ret:
            print("Error: Could not read frame.")
            return

        # Convert the frame to RGB format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to a PIL image
        img = Image.fromarray(frame)

        # Convert the PIL image to a PhotoImage
        imgtk = ImageTk.PhotoImage(image=img)

        # Display the image in the label
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
