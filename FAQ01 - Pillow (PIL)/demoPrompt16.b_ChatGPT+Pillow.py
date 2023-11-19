from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlButton, ControlFile
from PIL import Image
from io import BytesIO
from IPython.display import display

class ImageApp(BaseWidget):
    def __init__(self):
        super(ImageApp, self).__init__('Image Viewer')

        # Define PyForms controls
        self._btn_open = ControlButton('Open Image')
        self._file_open = ControlFile('File')

        # Bind event handlers
        self._btn_open.value = self.__btn_open_action
        self._file_open.changed_event = self.__file_open_changed

        # Set the form main widget
        self.formset = [
            ('_btn_open', '_file_open'),
        ]

    def __btn_open_action(self):
        self._file_open.click()

    def __file_open_changed(self):
        image_path = self._file_open.value

        if image_path:
            # Open and manipulate the image using Pillow
            pil_image = Image.open(image_path)
            pil_image.thumbnail((300, 300))  # Resize the image to fit within 300x300 pixels

            # Display the manipulated image (Note: this works in IPython/Jupyter)
            display(pil_image)

if __name__ == "__main__":
    from pyforms import start_app
    start_app(ImageApp)
