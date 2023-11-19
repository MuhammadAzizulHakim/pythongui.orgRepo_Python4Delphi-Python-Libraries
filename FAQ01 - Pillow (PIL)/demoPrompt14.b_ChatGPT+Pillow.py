import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide2.QtGui import QPixmap
from PIL import Image

class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create a QLabel to display the image
        self.image_label = QLabel(central_widget)
        layout.addWidget(self.image_label)

        # Create a QPushButton to open an image
        open_button = QPushButton("Open Image", central_widget)
        layout.addWidget(open_button)
        open_button.clicked.connect(self.openImage)

        central_widget.setLayout(layout)

    def openImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff);;All Files (*)", options=options
        )

        if file_path:
            image = Image.open(file_path)
            pixmap = QPixmap.fromImage(ImageQt.ImageQt(image))
            self.image_label.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    viewer = ImageApp()
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
