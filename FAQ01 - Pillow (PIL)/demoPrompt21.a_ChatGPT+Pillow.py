from PIL import Image
import flexx
from flexx import flx
import io
import base64

img = Image.open("C:/Users/ASUS/Pillow+ChatGPT/cat3.jpg")
buffer = io.BytesIO()
img.save(buffer, format="JPEG")
data_url = "data:image/jpeg;base64," + base64.b64encode(buffer.getvalue()).decode()

class CatImage(flx.Widget):
    def init(self):
        with flx.HBox():
            flx.ImageWidget(source=data_url)

#flx.run()

if __name__ == '__main__':
    app = flx.App(CatImage)
    app.launch('app')  # Open in the browser at http://localhost:3333/app
    flx.run()