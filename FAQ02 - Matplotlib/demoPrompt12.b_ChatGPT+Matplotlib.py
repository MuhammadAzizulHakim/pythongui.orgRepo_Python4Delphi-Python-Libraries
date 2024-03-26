import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib.figure import Figure
import numpy as np

# Define the Kivy application
class MatplotlibApp(App):
    def build(self):
        # Create a BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Create a Matplotlib figure
        figure = Figure()
        ax = figure.add_subplot(111)
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)

        # Create a FigureCanvasKivyAgg widget
        canvas = FigureCanvasKivyAgg(figure)

        # Add the canvas to the layout
        layout.add_widget(canvas)

        return layout

# Run the application
if __name__ == '__main__':
    MatplotlibApp().run()
