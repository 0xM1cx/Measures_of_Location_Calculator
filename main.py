import customtkinter
import tkinter as tk
class Calculator_Screen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
    
        self.configure(bg='#333333')
        label = tk.Label(self, text="test")
        label.pack()

class Calculator_Buttons(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Disk Scheduling Algorithm")
        self.geometry("450x700")
        self.columnconfigure((0, 1), weight=1)
        brand_font = customtkinter.CTkFont(family='Eurostile', size=27)
        calculator_Brand = customtkinter.CTkLabel(self, text="B4S1C C4LC", font=brand_font)
        calculator_Brand.grid(row=0, column=0, sticky="ew", padx=5, pady=20)

        screen = Calculator_Screen(self)

        buttons = Calculator_Buttons(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()