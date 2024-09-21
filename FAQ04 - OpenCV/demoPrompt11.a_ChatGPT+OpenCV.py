import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PIL import Image

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenCV with PyQt")
        self.setGeometry(100, 100, 800, 600)

        # Load an image using OpenCV
        cv_img = cv2.cvtColor(cv2.imread('got.jpg'), cv2.COLOR_BGR2RGB)

        # Convert the image to QImage
        height, width, channel = cv_img.shape
        bytes_per_line = 3 * width
        q_img = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Create a QLabel to display the image
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap.fromImage(q_img))

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())
