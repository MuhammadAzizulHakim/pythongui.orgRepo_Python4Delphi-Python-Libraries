import PySimpleGUI as sg
import PIL.Image
import io
import base64
def convert_to_bytes(file_or_bytes, resize=None):
   img = PIL.Image.open(file_or_bytes)
   with io.BytesIO() as bio:
      img.save(bio, format="PNG")
      del img
      return bio.getvalue()

imgdata = convert_to_bytes("C:/Users/ASUS/Pillow+ChatGPT/havanese_157.jpg")
layout = [[sg.Image(key='-IMAGE-', data=imgdata)]]
window = sg.Window('PIL based Image Viewer', layout,resizable=True)
while True:
   event, values = window.read()
   if event == sg.WIN_CLOSED:
      break
window.close()