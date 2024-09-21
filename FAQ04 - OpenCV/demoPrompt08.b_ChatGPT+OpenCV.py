from delphivcl import *
import cv2
import numpy as np

class MainForm(Form):

    def __init__(self, owner):
        self.Caption = "OpenCV with DelphiVCL4Python"
        self.SetBounds(100, 100, 800, 600)

        self.Image = Image(self)
        self.Image.Parent = self
        self.Image.SetBounds(10, 10, 640, 480)

        self.Button = Button(self)
        self.Button.Parent = self
        self.Button.SetBounds(660, 10, 120, 40)
        self.Button.Caption = "Capture Image"
        self.Button.OnClick = self.ButtonOnClick

    def ButtonOnClick(self, Sender):
        # Capture video from camera
        cap = cv2.VideoCapture(0)  # Use 0 for the default camera

        if not cap.isOpened():
            print("Error: Could not open video.")
            return

        # Read one frame
        ret, frame = cap.read()
        cap.release()

        if not ret:
            print("Error: Could not read frame.")
            return

        # Convert the frame to BMP format
        _, buffer = cv2.imencode(".bmp", frame)
        bmp_data = buffer.tobytes()

        # Load the image into the TImage component
        stream = MemoryStream(len(bmp_data))
        stream.Write(bmp_data)
        stream.Position = 0
        self.Image.Picture.Bitmap.LoadFromStream(stream)
        stream.Free()

def main():
    Application.Initialize()
    Application.Title = "DelphiVCL4Python with OpenCV"
    main_form = MainForm(Application)
    Application.Run()

main()
