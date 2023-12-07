import tkinter as tk
from tkinter import messagebox
import numpy as np

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Statistics Calculator")
        self.geometry("800x600")

        # Calculator Name Label
        label_name = tk.Label(self, text="Statistics Calculator", font=("Arial", 16))
        label_name.pack(pady=10)

        # Screen for Results
        self.result_screen = tk.Entry(self, font=("Arial", 18), justify="right", bd=10, insertwidth=4)
        self.result_screen.pack(fill="both", expand=True)

        # Screen for Input
        self.input_screen = tk.Entry(self, font=("Arial", 18), justify="right", bd=10, insertwidth=4)
        self.input_screen.pack(fill="both", expand=True)

        # Table input
        table_label = tk.Label(self, text="Enter numbers separated by spaces:")
        table_label.pack(pady=5)

        self.table_input = tk.Entry(self, font=("Arial", 14))
        self.table_input.pack(pady=10)

        # Calculator Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(expand=True, fill="both")

        # Define button layout
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('Del', 4, 0), ('Stats', 4, 1)  # Added a delete button and stats button
        ]

        # Create buttons
        for (text, row, column) in buttons:
            button = tk.Button(button_frame, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky="nsew")

        # Configure button frame to expand proportionally
        for i in range(5):
            button_frame.columnconfigure(i, weight=1)
            button_frame.rowconfigure(i, weight=1)

        # Set default values
        self.current_input = ""
        self.current_result = ""
        self.operator = ""

        # List to store table data
        self.table_data = []

    def on_button_click(self, button_text):
        if button_text.isdigit() or button_text == '.':
            self.current_input += button_text
        elif button_text == 'C':
            self.current_input = ""
            self.current_result = ""
            self.operator = ""
        elif button_text == 'Del':
            self.current_input = self.current_input[:-1]  # Delete the last character
        elif button_text == 'Stats':
            self.calculate_statistics()
        elif button_text == '=':
            if self.current_input and self.operator:
                try:
                    result = eval(f"{self.current_result}{self.operator}{self.current_input}")
                    self.current_result = str(result)
                    self.current_input = ""
                    self.operator = ""
                except Exception as e:
                    self.current_result = "Error"
                    self.current_input = ""
                    self.operator = ""

        # Update screens
        self.update_screens()

    def update_screens(self):
        self.result_screen.delete(0, tk.END)
        self.result_screen.insert(0, self.current_result)

        self.input_screen.delete(0, tk.END)
        self.input_screen.insert(0, self.current_input)

    def calculate_statistics(self):
        try:
            # Parse input from table
            table_values = self.table_input.get().split()
            self.table_data = [float(value) for value in table_values]

            if not self.table_data:
                messagebox.showinfo("Error", "Please enter numbers in the table.")
                return

            # Calculate statistics using numpy
            mean = np.mean(self.table_data)
            median = np.median(self.table_data)
            quartiles = np.percentile(self.table_data, [25, 50, 75])
            deciles = np.percentile(self.table_data, range(10, 100, 10))
            percentiles = np.percentile(self.table_data, range(1, 100))

            # Display the sorted data in ascending order
            sorted_data = sorted(self.table_data)
            sorted_str = ', '.join(map(str, sorted_data))

            # Underline the positions of measures of location
            result_str = f"Sorted Data: {sorted_str}\n\n"
            result_str += f"Mean: {mean:.2f}\n"
            result_str += f"Median: {median:.2f}\n"
            result_str += f"Quartiles (Q1, Q2, Q3): {quartiles}\n"
            result_str += f"Deciles: {deciles}\n"
            result_str += f"Percentiles: {percentiles}"

            # Display the result in a new window
            result_window = tk.Toplevel(self)
            result_window.title("Statistics Result")
            result_label = tk.Label(result_window, text=result_str, font=("Arial", 12))
            result_label.pack(padx=20, pady=20)

        except ValueError:
            messagebox.showinfo("Error", "Please enter valid numbers in the table.")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()