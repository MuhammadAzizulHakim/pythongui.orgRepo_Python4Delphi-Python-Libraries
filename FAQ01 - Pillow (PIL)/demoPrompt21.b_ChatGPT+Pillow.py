from flexx import flx

class ImageViewer(flx.Widget):

    def init(self):
        # Create a button to trigger image loading
        self.button = flx.Button(text='Load Image')
        self.button.clicked.connect(self.load_image)

        # Create an image widget to display the loaded image
        self.image_widget = flx.ImageWidget()

        # Create a VBox layout to organize the widgets vertically
        with flx.VBox():
            flx.Label(text='Image Viewer')
            self.button
            self.image_widget

    def load_image(self):
        # Simulate image loading by fetching an image from a URL
        image_url = 'https://fastly.picsum.photos/id/461/200/300.jpg?hmac=dIwmQxeVflRD0QrOZ_p0_q-LpAY7sVhua6FCEIR_xi8'
        self.image_widget.set_source(image_url)

if __name__ == '__main__':
    app = flx.App(ImageViewer)
    app.launch('app')  # Open in the browser at http://localhost:3333/app
    flx.run()
