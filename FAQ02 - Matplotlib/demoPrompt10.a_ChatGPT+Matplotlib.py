# Import the matplotlib.pyplot and tkinter modules
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import matplotlib.pyplot as plt
import tkinter as tk
#from matplotlib import FigureCanvasTkAgg

# Create a Tkinter window
window = tk.Tk()
window.title('Matplotlib Example')
window.geometry('500x500')

# Create a Tkinter frame
frame = tk.Frame(window)
frame.pack()

# Create some sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a Matplotlib figure and an axes object
fig, ax = plt.subplots()

# Plot the data as a line
ax.plot(x, y)

# Set the plot title and axis labels
ax.set_title('Example of Line Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Embed the Matplotlib figure into the Tkinter frame
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Add a Matplotlib toolbar to the Tkinter window
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack()

# Show the Tkinter window
window.mainloop()
