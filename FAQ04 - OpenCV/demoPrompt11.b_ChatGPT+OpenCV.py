import cv2
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import numpy as np

class ImageProcessor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenCV with PyQt - Image Processing")
        self.setGeometry(100, 100, 1200, 600)

        # Central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout(self.central_widget)

        # Original image display label
        self.original_label = QLabel(self)
        self.layout.addWidget(self.original_label)

        # Processed image display label
        self.processed_label = QLabel(self)
        self.layout.addWidget(self.processed_label)

        # Load image button
        self.load_button = QPushButton("Load Image", self)
        self.load_button.clicked.connect(self.load_image)
        self.layout.addWidget(self.load_button)

        # Grayscale button
        self.grayscale_button = QPushButton("Convert to Grayscale", self)
        self.grayscale_button.clicked.connect(self.convert_grayscale)
        self.layout.addWidget(self.grayscale_button)

        # Canny Edge Detection button
        self.canny_button = QPushButton("Apply Canny Edge Detection", self)
        self.canny_button.clicked.connect(self.apply_canny)
        self.layout.addWidget(self.canny_button)

        self.image = None
        self.processed_image = None

    def load_image(self):
        # Open file dialog to choose an image file
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.bmp)")
        if file_name:
            # Load the image using OpenCV
            self.image = cv2.imread(file_name)
            self.display_image(self.image, self.original_label)

    def display_image(self, img, label):
        # Convert the image to RGB format for display in PyQt
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img_rgb.shape
        bytes_per_line = 3 * width
        qimg = QImage(img_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)

        # Display the image in the QLabel
        label.setPixmap(pixmap)
        label.setScaledContents(True)

    def convert_grayscale(self):
        if self.image is not None:
            # Convert the image to grayscale
            self.processed_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

            # Convert grayscale image to QImage format for display
            height, width = self.processed_image.shape
            bytes_per_line = width
            qimg = QImage(self.processed_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qimg)

            # Display the processed image
            self.processed_label.setPixmap(pixmap)
            self.processed_label.setScaledContents(True)

    def apply_canny(self):
        if self.image is not None:
            # Convert to grayscale first, then apply Canny edge detection
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.processed_image = cv2.Canny(gray, 100, 200)

            # Convert edge-detected image to QImage format for display
            height, width = self.processed_image.shape
            bytes_per_line = width
            qimg = QImage(self.processed_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qimg)

            # Display the processed image
            self.processed_label.setPixmap(pixmap)
            self.processed_label.setScaledContents(True)

    def closeEvent(self, event):
        # Perform cleanup, if needed, when the application window is closed
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageProcessor()
    window.show()
    sys.exit(app.exec_())
