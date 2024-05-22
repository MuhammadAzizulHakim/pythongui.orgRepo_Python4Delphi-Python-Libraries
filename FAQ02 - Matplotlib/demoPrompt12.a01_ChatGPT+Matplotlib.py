import sys
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

class MyKivyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Example data
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)

        # Create a Matplotlib figure
        fig, ax = plt.subplots()
        ax.plot(x, y, label='Sine Wave')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Matplotlib Plot in Kivy')
        ax.grid(True)
        ax.legend()

        # Add the Matplotlib canvas to the Kivy layout
        canvas = FigureCanvasKivyAgg(fig)
        layout.add_widget(canvas)

        return layout

if __name__ == '__main__':
    MyKivyApp().run()
