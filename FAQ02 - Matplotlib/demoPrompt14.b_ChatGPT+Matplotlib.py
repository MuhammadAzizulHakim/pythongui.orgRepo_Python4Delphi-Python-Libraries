import matplotlib
matplotlib.use('Qt5Agg')  # Use Qt5Agg backend
import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Matplotlib with PySide")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a Matplotlib figure and canvas
        self.figure = plt.figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Plot initial data
        self.plot_data()

    def plot_data(self):
        # Generate some sample data
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Clear previous plot
        self.figure.clear()

        # Plot data using Matplotlib
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Matplotlib Plot')

        # Update canvas
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
