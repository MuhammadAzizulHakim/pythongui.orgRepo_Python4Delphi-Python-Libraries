import tkinter as tk
from tkinter import ttk
import numpy as np

class NumPyTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NumPy with Tkinter")

        # Create a frame
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Create a label
        self.label = ttk.Label(self.frame, text="NumPy Array:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        # Create an entry widget
        self.entry = ttk.Entry(self.frame)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        # Create a button to compute the mean
        self.button = ttk.Button(self.frame, text="Compute Mean", command=self.compute_mean)
        self.button.grid(row=1, columnspan=2, padx=5, pady=5)

        # Create a label to display the result
        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.grid(row=2, columnspan=2, padx=5, pady=5)

    def compute_mean(self):
        # Get the input from the entry widget
        input_text = self.entry.get()

        try:
            # Convert the input to a NumPy array
            arr = np.array(eval(input_text))

            # Compute the mean of the array
            mean_value = np.mean(arr)

            # Display the mean value
            self.result_label.config(text=f"Mean: {mean_value}")
        except Exception as e:
            # Display an error message if input is invalid
            self.result_label.config(text="Error: Invalid input")

def main():
    root = tk.Tk()
    app = NumPyTkinterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
