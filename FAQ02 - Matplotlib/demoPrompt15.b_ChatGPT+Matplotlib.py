import matplotlib
matplotlib.use('Qt5Agg')
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_plot(window):
    # Generate some sample data
    x = [1, 2, 3, 4, 5]
    y = [10, 5, 15, 7, 10]

    # Create a Matplotlib figure and plot
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Matplotlib Plot')

    # Convert Matplotlib figure to Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=window['-CANVAS-'].TKCanvas)

    # Update the PySimpleGUI window with the Matplotlib canvas
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
    canvas.draw()

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close':
            break

    plt.close(fig)

def main():
    # Define PySimpleGUI layout
    layout = [[sg.Canvas(key='-CANVAS-')],
              [sg.Button('Close')]]

    # Create PySimpleGUI window
    window = sg.Window('Matplotlib with PySimpleGUI', layout, finalize=True, resizable=True)

    # Call draw_plot function with the PySimpleGUI window
    draw_plot(window)

    # Close the PySimpleGUI window
    window.close()

if __name__ == '__main__':
    main()
