import tkinter as tk
from tkinter import ttk
import numpy as np

class MatrixCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")

        # Create UI components
        self.label_matrix_a = ttk.Label(root, text="Matrix A:")
        self.entry_matrix_a = ttk.Entry(root, width=20)
        self.label_matrix_b = ttk.Label(root, text="Matrix B:")
        self.entry_matrix_b = ttk.Entry(root, width=20)
        self.btn_add = ttk.Button(root, text="Add", command=self.perform_addition)
        self.btn_multiply = ttk.Button(root, text="Multiply", command=self.perform_multiplication)
        self.result_label = ttk.Label(root, text="Result:")

        # Arrange UI components using grid layout
        self.label_matrix_a.grid(row=0, column=0, padx=10, pady=5)
        self.entry_matrix_a.grid(row=0, column=1, padx=10, pady=5)
        self.label_matrix_b.grid(row=1, column=0, padx=10, pady=5)
        self.entry_matrix_b.grid(row=1, column=1, padx=10, pady=5)
        self.btn_add.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.btn_multiply.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    def perform_addition(self):
        try:
            matrix_a = np.array(eval(self.entry_matrix_a.get()))
            matrix_b = np.array(eval(self.entry_matrix_b.get()))
            result = matrix_a + matrix_b
            self.result_label.config(text=f"Result: {result}")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def perform_multiplication(self):
        try:
            matrix_a = np.array(eval(self.entry_matrix_a.get()))
            matrix_b = np.array(eval(self.entry_matrix_b.get()))
            result = np.dot(matrix_a, matrix_b)
            self.result_label.config(text=f"Result: {result}")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculatorApp(root)
    root.mainloop()
