import wx
from wx import Image as wxImage
from wx import ImageFromStream, BitmapFromImage
from io import BytesIO
from PIL import Image as PILImage, ImageTk

# Import your wxGlade-generated code
from my_gui_wxglade import MyFrame1

class MyFrameModified(MyFrame1):
    def __init__(self, *args, **kwds):
        MyFrame1.__init__(self, *args, **kwds)
        
    def open_image(self, event):
        dlg = wx.FileDialog(self, "Choose an image file", wildcard="Image files (*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff)|*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff", style=wx.FD_OPEN)
        
        if dlg.ShowModal() == wx.ID_OK:
            file_path = dlg.GetPath()
            
            # Open and manipulate the image using Pillow
            pil_image = PILImage.open(file_path)
            pil_image.thumbnail((300, 300))  # Resize the image to fit within 300x300 pixels

            # Convert the Pillow image to a wx.Image
            image_stream = BytesIO()
            pil_image.save(image_stream, format="PNG")
            wx_image = ImageFromStream(image_stream)

            # Convert the wx.Image to a wx.Bitmap
            wx_bitmap = BitmapFromImage(wx_image)

            # Update the wx.StaticBitmap
            self.m_bitmap1.SetBitmap(wx_bitmap)

        dlg.Destroy()

if __name__ == '__main__':
    app = wx.App(0)
    frame = MyFrameModified(None, wx.ID_ANY, "")
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()
