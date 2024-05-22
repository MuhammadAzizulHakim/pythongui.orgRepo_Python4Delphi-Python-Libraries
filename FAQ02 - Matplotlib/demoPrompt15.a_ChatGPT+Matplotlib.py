import matplotlib
matplotlib.use('Qt5Agg')
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Generate some sample data
x_values = np.linspace(0, 10, 100)
y_values = np.sin(x_values)

# Create a Matplotlib figure and plot
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x_values, y_values, label="sin(x)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Matplotlib Plot in PySimpleGUI")

# Create the PySimpleGUI layout
layout = [
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button("Exit")]
]

# Create the PySimpleGUI window
window = sg.Window("Matplotlib Plot Example", layout, finalize=True)

# Embed the Matplotlib plot in the PySimpleGUI canvas
canvas_elem = window["-CANVAS-"]
canvas = FigureCanvasTkAgg(fig, master=canvas_elem.Widget)
canvas.draw()
canvas.get_tk_widget().pack(side="top", fill="both", expand=1)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
