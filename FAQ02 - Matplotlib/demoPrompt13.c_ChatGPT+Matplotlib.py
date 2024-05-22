import wx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 400))

        # Create a panel
        self.panel = wx.Panel(self)

        # Create a Matplotlib figure
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        # Generate some data
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Plot the data
        self.axes.plot(x, y)

        # Create a FigureCanvas
        self.canvas = FigureCanvas(self.panel, -1, self.figure)

        # Create a vertical box sizer to manage layout
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)

        # Set sizer for the panel
        self.panel.SetSizer(self.sizer)

        # Add the panel to the frame
        self.sizer.Fit(self)
        self.Centre()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title='Matplotlib with wxPython')
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
