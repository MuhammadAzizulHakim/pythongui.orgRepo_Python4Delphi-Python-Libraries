from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from PIL import Image as PILImage

class ImageApp(App):
    def build(self):
        # Create a Kivy layout
        layout = BoxLayout(orientation='vertical')

        # Load and manipulate the image using Pillow
        image_path = "C:/Users/ASUS/Pillow+ChatGPT/penguin.jpg"
        pil_image = PILImage.open(image_path)
        pil_image.thumbnail((300, 300))  # Resize the image to fit within 300x300 pixels
        pil_image.save("C:/Users/ASUS/Pillow+ChatGPT/resized_penguinImage.jpg")  # Save the manipulated image

        # Display the manipulated image in Kivy
        kivy_image = Image(source="C:/Users/ASUS/Pillow+ChatGPT/resized_penguinImage.jpg")
        layout.add_widget(kivy_image)

        return layout

if __name__ == '__main__':
    ImageApp().run()
