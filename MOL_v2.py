import tkinter as tk
from statistics import quantiles

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Input Calculator")
        self.input_var = tk.StringVar()
        self.data_array = []
        self.decile_array = []
        self.data_input_mode = False
        self.create_ui()

    def create_ui(self):
        # Entry widget for input
        input_frame = tk.Frame(self.master)
        input_frame.grid(row=0, column=0, columnspan=4)
        entry = tk.Entry(input_frame, textvariable=self.input_var, justify='right', font=('Arial', 14), bd=10)
        entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky='news')

        # Calculator buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('Data', 5, 0), ('AC', 5, 1), ('Quartile', 5, 2), ('Del', 5, 3), ('Decile', 5, 4), ('Percentile', 5, 5)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, command=lambda t=text: self.on_button_click(t), font=('Arial', 14))
            button.grid(row=row, column=col, ipadx=8, ipady=8, sticky='news')

    def on_button_click(self, value):
        if value == 'C':
            self.input_var.set('')
        elif value == '=':
            if self.data_input_mode:
                # Add a space when "=" is clicked in data input mode
                current_input = self.input_var.get().strip()
                self.input_var.set(current_input + ' ')
            elif self.decile_array and self.input_var.get().startswith('Decile: '):
                # Compute the decile of each number in the Decile array
                self.compute_deciles()
        elif value == 'Data':
            # Enable data input mode
            self.data_input_mode = True
            self.input_var.set('Data: ')
        elif value == 'AC':
            if self.input_var.get().startswith('Decile: '):
                # Store the input in the Decile array
                self.store_decile()
            else:
                # Store the data in the Data array
                self.store_data()
            self.input_var.set('')  # Clear the screen
        elif value == 'Del':
            # Delete one character
            current_input = self.input_var.get().strip()
            new_input = current_input[:-1]
            self.input_var.set(new_input)
        elif value == 'Decile':
            # Display "Decile: " on the screen and clear the input
            self.data_input_mode = False
            self.input_var.set('Decile: ')
            self.decile_array = []
        elif value in ['Quartile', 'Percentile']:
            # Disable data input mode and set the location measure
            self.data_input_mode = False
            self.input_var.set(f"{value}: ")
        else:
            current_input = self.input_var.get()
            new_input = current_input + value
            self.input_var.set(new_input)

    def store_data(self):
        data_input = self.input_var.get().strip()
        data_list = data_input.replace('Data: ', '').split()
        self.data_array.extend(data_list)

    def store_decile(self):
        decile_input = self.input_var.get().strip()
        decile_list = decile_input.replace('Decile: ', '').split()
        self.decile_array.extend(decile_list)

    def compute_deciles(self):
        try:
            data_list = sorted([float(x) for x in self.data_array])
            decile_results = [quantiles(data_list, n=10, p=float(x)) for x in self.decile_array]
            self.input_var.set(f"Decile results: {', '.join(map(str, decile_results))}")
            self.decile_array = []
        except Exception as e:
            pass  # Handle the case where the input is not in the expected format

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
