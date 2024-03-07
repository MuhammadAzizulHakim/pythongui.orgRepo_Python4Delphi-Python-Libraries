import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

def plot_matplotlib():
    # Create sample data
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    # Create a Matplotlib figure
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, label='Sine Wave')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Matplotlib Plot')
    ax.legend()

    # Embed the Matplotlib figure in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create the main Tkinter window
root = tk.Tk()
root.title("Tkinter with Matplotlib")

# Create a frame within the window
frame = ttk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

# Create a button to trigger Matplotlib plot
button = ttk.Button(frame, text="Plot Matplotlib", command=plot_matplotlib)
button.pack(side=tk.BOTTOM)

# Start the Tkinter event loop
root.mainloop()
