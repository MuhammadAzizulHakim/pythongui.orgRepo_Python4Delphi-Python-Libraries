from PySide6 import QtWidgets, QtGui, QtCore
from PIL import Image, ImageQt

app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()

window.setWindowTitle("Pillow with PySide GUI")
window.resize(500, 500)
window.move(100, 100)

label = QtWidgets.QLabel(window)
label.setAlignment(QtCore.Qt.AlignCenter)
label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

img = Image.open("C:/Users/ASUS/Pillow+ChatGPT/havanese_157.jpg")
qimg = ImageQt.ImageQt(img)
qpix = QtGui.QPixmap.fromImage(qimg)

label.setPixmap(qpix)

window.show()
app.exec_()
