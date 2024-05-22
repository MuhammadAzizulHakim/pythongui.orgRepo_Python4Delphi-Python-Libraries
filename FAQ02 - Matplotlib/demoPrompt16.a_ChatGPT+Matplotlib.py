# my_app.py
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlButton
from pyforms.controls import ControlMatplotlib  # Import the Matplotlib control

class MyApp(BaseWidget):
    def __init__(self):
        super().__init__('My Matplotlib App')
        self.set_margin(10)

        # Create a Matplotlib control
        self.plot_widget = ControlMatplotlib('Plot')

        # Create a button to update the plot
        self.update_button = ControlButton('Update Plot', default=self._update_plot)

        # Add controls to the form
        self.formset = [
            ('plot_widget', 'update_button'),
        ]

    def _update_plot(self):
        # Example: Update the Matplotlib plot when the button is clicked
        x = [1, 2, 3, 4, 5]
        y = [10, 8, 6, 4, 2]
        self.plot_widget.value.plot(x, y)
        self.plot_widget.value.set_title('My Custom Plot')
        self.plot_widget.repaint()

if __name__ == '__main__':
    pyforms.start_app(MyApp)
