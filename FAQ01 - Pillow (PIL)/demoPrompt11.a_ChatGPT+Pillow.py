from PIL import Image, ImageQt
from PyQt5 import QtWidgets, QtGui, QtCore

app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()

window.setWindowTitle("Pillow with PyQt")
window.resize(500, 500)
window.move(100, 100)

label = QtWidgets.QLabel()
label.setAlignment(QtCore.Qt.AlignCenter)
label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

img = Image.open("C:/Users/ASUS/Pillow+ChatGPT/cat4.jpg")
qimg = ImageQt.ImageQt(img)
qpix = QtGui.QPixmap.fromImage(qimg)
label.setPixmap(qpix)

window.setCentralWidget(label)

window.show()
app.exec_()
