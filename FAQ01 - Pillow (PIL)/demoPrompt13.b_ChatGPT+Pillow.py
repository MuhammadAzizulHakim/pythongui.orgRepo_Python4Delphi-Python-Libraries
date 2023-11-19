import wx
from PIL import Image
import io

class ImageFrame(wx.Frame):
    def __init__(self, parent, title):
        super(ImageFrame, self).__init__(parent, title=title, size=(400, 300))

        self.panel = wx.Panel(self)
        self.image = self.load_image("C:/Users/ASUS/Pillow+ChatGPT/penguin2.jpg")
        self.display_image()

    def load_image(self, image_path):
        with open(image_path, 'rb') as image_file:
            image_data = io.BytesIO(image_file.read())
        return Image.open(image_data)

    def display_image(self):
        image = wx.Image(self.image.size[0], self.image.size[1])
        image.SetData(self.image.tobytes())
        bitmap = wx.Bitmap(image)
        wx.StaticBitmap(self.panel, -1, bitmap, (10, 10), (bitmap.GetWidth(), bitmap.GetHeight()))

if __name__ == '__main__':
    app = wx.App(False)
    frame = ImageFrame(None, "Image Viewer")
    frame.Show()
    app.MainLoop()
