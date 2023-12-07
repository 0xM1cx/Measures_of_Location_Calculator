import tkinter as tk
from tkinter import ttk
from tkinter import font

foreground = "#b6e853"
background = "#1a1a1a"

class Calculator_Screen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        global foreground

        screen_bg = "#333333" 

        self.configure(bg='#333333')
        upperDigits = tk.Label(self, text="NumberScreen", font=("CASIO-Calculator-Font", 9), bg=screen_bg, fg='black')
        upperDigits.pack(side=tk.LEFT, padx=5, pady=10)

        inputDigits = tk.Entry(self, bg=screen_bg, border=None)
        inputDigits.pack(side=tk.LEFT, padx=5, pady=10)

class Calculator_Buttons(tk.Frame):
    def __init__(self, master):
        super().__init__(master)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Disk Scheduling Algorithm")
        self.geometry("450x700")
        self.configure(bg="#1a1a1a") 

        global foreground, background

        calculator_Brand = tk.Label(self, text="B4S1C C4LC", font=("CASIO-Calculator-Font", 15), bg=background, fg=foreground)
        calculator_Brand.pack(pady=20) 

        screen = Calculator_Screen(self)
        screen.pack(fill=tk.X)

if __name__ == "__main__":
    app = App()
    app.mainloop()