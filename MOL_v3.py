import customtkinter
import tkinter as tk
from tkinter import ttk
from time import sleep
import numpy as np

## Plotting Stuff
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

entries = []
watToFind = []
## Color palet ta
textColor = "#00C4F7"
results = {
    "Quartiles": [],
    "Percentiles": [],
    "Decile": []
}
data = []


class ComputeMeasuresOfLocation():
    pass


class InputWindow(customtkinter.CTkToplevel):
    def __init__(self, locToFind):
        super().__init__()
        self.geometry("400x300")
        font = customtkinter.CTkFont(family="Monaco, 'Bitstream Vera Sans Mono', 'Lucida Console', Terminal, monospace", size=30)
        self.label = customtkinter.CTkLabel(self, text=f"Give the nth {locToFind}", font=font)
        self.label.pack(padx=20, pady=20)


        if(locToFind == "Quartiles"):
            self.input = customtkinter.CTkComboBox(self, values=["1", "2", "3"])
            self.input.pack(side="top", expand=True, fill="x", padx=20, pady=20)
        elif(locToFind == "Deciles"):
            numbers = [str(i) for i in range(1, 11)]
            self.input = customtkinter.CTkComboBox(self, values=numbers)
            self.input.pack(side="top", expand=True, fill="x", padx=20, pady=20)
        elif(locToFind == "Percentiles"):
            numbers = [str(i) for i in range(1, 101)]
            self.input = customtkinter.CTkComboBox(self, values=numbers)
            self.input.pack(side="top", expand=True, fill="x", padx=20, pady=20)

        # self.input = customtkinter.CTkEntry(self, placeholder_text=f"Supply Some Input({locToFind})", text_color=textColor)
        # self.input.pack(side="top", expand=True, fill="x", padx=20, pady=20)
        
        self.sumbit = customtkinter.CTkButton(self, font=font, text="Sumbit", text_color=textColor, command=self.processInput)
        self.locToFind = locToFind
    def processInput(self):
        global watToFind
        watToFind = self.input.get().split(" ") 

        output = self.master.output
        output.display_data(self, self.locToFind, self.input.get())


class ErrorMessage(customtkinter.CTkToplevel):
    def __init__(self, *args):
        super().__init__(*args)
        self.geometry("500x500")
        font = customtkinter.CTkFont(family="Monaco, 'Bitstream Vera Sans Mono', 'Lucida Console', Terminal, monospace", size=20)
        self.label = customtkinter.CTkLabel(self, font=font, width = 100, height=100, text_color="#b5e853", text="The Requests must be within the outermost and innermost disk range")

class OUTPUT(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        

    def displayOutput(self, locToFind, n):
        # display data in a 10 column format
        data_str = ""
        counter = 0
        global data 
        for num in data:
            if counter % 10 == 0:
                data_str += " " + str(num) + "\n" 
            else:
                data_str += " " + num
            counter += 1

        display_data = customtkinter.CTkLabel(self, text=f"DATA: {data_str}", text_color=textColor) 
        display_data.pack(padx=10, pady=10)

        #display Result
        global results
        if "2" in n:
            n = f"{n}nd"
        elif "1" in n:
            n = f"{n}st"
        elif "3" in n:
            n = f"{n}rd"
        else:
            n = f"{n}nd"

        display_result = customtkinter.CTkLabel(self, text=f"The {n} {locToFind} => {results[locToFind][int(n)]}")

#### The widgets in the frames must be in a grid
class DataTable(customtkinter.CTkScrollableFrame):
    rowCounter = 0
    flag = True
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure((0), weight=1)

    def addData(self, target_frame, noOfRequests):
        global entries

        if len(entries) != 0:
            for entry in entries:
                entry.destroy()
            entries = []

        for i in range(noOfRequests):
                entry = customtkinter.CTkEntry(target_frame)
                entry.grid(row=self.rowCounter, column=0, pady=5, padx=80, sticky="ew")
                entries.append(entry)
                self.rowCounter += 1

class OptionMenu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        font = customtkinter.CTkFont(family="Monaco, 'Bitstream Vera Sans Mono', 'Lucida Console', Terminal, monospace", size=14)

        ### Input Data Button ###        
        self.noOfData = customtkinter.CTkEntry(self, font=font, text_color=textColor, placeholder_text="Number of Data")
        self.noOfData.grid(row=0, column=0, padx=10, pady=10)
        self.data = customtkinter.CTkButton(self, font=font, text_color=textColor, text="Add Data", fg_color="black", command=self.inputData)
        self.data.grid(row=1, column=0, padx=10, pady=10)

        ### Measures of Location Button
        quartile_label = customtkinter.CTkLabel(self, font=font, text_color=textColor, text="Solve for Quartile") 
        quartile_label.grid(row=0, column=1, padx=10, pady=10)
        self.Quartile = customtkinter.CTkButton(self, text="Quartile", command=self.calculateQuartile, text_color=textColor, fg_color="black")
        self.Quartile.grid(row=1, column=1, padx=10, pady=10)


        decile_label = customtkinter.CTkLabel(self, font=font, text="Solve for Decile", text_color=textColor)
        decile_label.grid(row=0, column=2, padx=10, pady=10)
        self.Decile = customtkinter.CTkButton(self, text="Decile", text_color=textColor, command=self.calculateDecile, fg_color="black")
        self.Decile.grid(row=1, column=2, padx=10, pady=10)


        percentile_label = customtkinter.CTkLabel(self, font=font, text="Solve for Percentile", text_color=textColor)
        percentile_label.grid(row=0, column=3, padx=10, pady=10)
        self.Percentile = customtkinter.CTkButton(self, text="Percentile", text_color=textColor, command=self.calculatePercentile, fg_color='black')
        self.Percentile.grid(row=1, column=3, padx=10, pady=10)

        storeData_label = customtkinter.CTkLabel(self, font=font, text="Save Data", text_color=textColor)
        storeData_label.grid(row=0, column=4, padx=10, pady=10)
        self.storeData = customtkinter.CTkButton(self, text="Save", fg_color='black', text_color=textColor, command=self.SaveData)
        self.storeData.grid(row=1, column=4, padx=10, pady=10)

        #top level window flag
        self.toplevel_window = None


    def SaveData(self):
        global data
        self.data = [int(entry.get()) for entry in entries]
        data = self.data


    def calculateQuartile(self):
        global entries, results
        array_data = self.data
        sorted_data = np.sort(array_data)
        
        Q1 = np.percentile(sorted_data, 25)
        Q2 = np.percentile(sorted_data, 50)
        Q3 = np.percentile(sorted_data, 75)
        results["Quartiles"] = []
        results["Quartiles"].append(Q1)
        results["Quartiles"].append(Q2)
        results["Quartiles"].append(Q3)


        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = InputWindow("Quartiles")  
        else:
            self.toplevel_window.focus()

    def calculatePercentile(self):
        global entries, results
        array_data = self.data
        sorted_data = np.sort(array_data)
        percentiles = [np.percentile(sorted_data, i) for i in range(1, 101)]
        results["Percentiles"] = percentiles


        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = InputWindow("Percentiles")  
        else:
            self.toplevel_window.focus()

    def calculateDecile(self):
        global entries, results
        array_data = self.data
        sorted_data = np.sort(array_data)
        deciles = [np.percentile(sorted_data, i) for i in range(10, 100, 10)]
        results["Decile"] = deciles


        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = InputWindow("Deciles")  
        else:
            self.toplevel_window.focus()


    def inputData(self):
        data = DataTable(self)
        data.addData(target_frame=self.master.dataFrame, noOfRequests=int(self.noOfData.get()))

    def removeAllInput(self):
        self.NumRequest.delete("0.0", "end")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Disk Scheduling Algorithm")
        self.geometry("900x600")
        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        # self.iconbitmap("./icon.ico")

        self.optionMenu = OptionMenu(self)
        self.optionMenu.grid(row=1, column=0, sticky="ew", columnspan=2, padx=20, pady=20)
        
        self.dataFrame = DataTable(self)
        self.dataFrame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
 
        self.output = OUTPUT(self)
        self.output.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()