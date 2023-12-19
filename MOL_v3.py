import customtkinter
import numpy as np
from MOL_CALCULATOR import ComputeDecile, ComputePercentile, ComputeQuartile
entries = []
## Color palet ta
textColor = "#00C4F7"
results = {
    "Quartiles": [],
    "Percentiles": [],
    "Deciles": []
}
data = []

'''
# TODO
1. Add pointing down arrows at the results lable
2. Fix the computation
'''

class InputWindow(customtkinter.CTkToplevel):
    def __init__(self, locToFind):
        super().__init__()
        self.geometry("400x300")
        self.title("What To Find?")
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
        
        self.sumbit = customtkinter.CTkButton(self, text="Sumbit", text_color=textColor, command=self.processInput, fg_color='black')
        self.sumbit.pack(side="top", padx=10, pady=10)

        self.locToFind = locToFind


    def processInput(self):
        global watToFind
        watToFind = self.input.get().split(" ") 

        output = self.master.output
        output.displayOutput(self.locToFind, self.input.get())

class OUTPUT(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

    def clear_frame(self):
        # Destroy all child widgets in the frame
        for widget in self.winfo_children():
            widget.destroy()

    def displayOutput(self, locToFind, n):
        # display unsorted data in a 10 column format
        font = customtkinter.CTkFont(family="Monaco, 'Bitstream Vera Sans Mono', 'Lucida Console', Terminal, monospace", size=15)
        self.clear_frame()

        data_str = ""
        counter = 0
        global data
        global results
        if len(data) > 10: 
            for num in data:
                if counter % 10 == 0 and counter != 1:
                    data_str += " " + str(num) + "\n" 
                else:
                    data_str += " " + str(num)
                counter += 1
        else:
            data = [str(x) for x in data]
            data_str = " ".join(data)

        display_data = customtkinter.CTkLabel(self, font=font, text=f"UNSORTED DATA:\n{data_str}", text_color=textColor) 
        display_data.pack(padx=10, pady=10)

        # Display sorted Data
        sorted_data_str = ""
        _counter = 0
        converted_data = [int(i) for i in data]
        sorted_data = sorted(converted_data)
        if len(sorted_data) > 10:
            for _num in sorted_data:
                if _counter % 10 == 0 and _counter != 1:
                    sorted_data_str += " " + str(_num) + "\n"
                else:
                    sorted_data_str += " " + str(_num)
                _counter += 1
        else:
            _data_ = [str(x) for x in sorted_data]
            sorted_data_str = " ".join(_data_)

        display_sorted_data = customtkinter.CTkLabel(self, font=font, text=f"SORTED DATA:\n{sorted_data_str}", text_color=textColor)
        display_sorted_data.pack(padx=10, pady=10) 



        #display Result
        if "2" in n[-1]:
            n_word = f"{n}nd"
        elif "1" in n[-1]:
            n_word = f"{n}st"
        elif "3" in n[-1]:
            n_word = f"{n}rd"
        else:
            n_word = f"{n}th"



        if locToFind == "Deciles":
            results['Deciles'].clear()
            res, flag = ComputeDecile(sorted_data, int(n))
            if flag == True:
                results["Deciles"].append((res, res))
            else:
                results["Deciles"].append((round(res), res))
        elif locToFind == "Percentiles":
            results["Percentiles"].clear()
            res, flag = ComputePercentile(sorted_data, int(n))
            if flag == True:
                results["Percentiles"].append((res, res))
            else:
                results["Percentiles"].append((round(res), res))
        # display_result = customtkinter.CTkLabel(self, text=f"The {n_word} {locToFind} => {results[locToFind][int(n)-1][0]}", text_color=textColor)
        # display_result.pack(padx = 20, pady=20)

        if locToFind == "Quartiles":
            display_computation_result = customtkinter.CTkLabel(self, font=font, text=f"The result of the computation was: \n{results[locToFind][int(n)-1][1]}", text_color=textColor)
            display_computation_result.pack(padx=20, pady=20)
        elif locToFind == "Deciles":
            display_computation_result = customtkinter.CTkLabel(self, font=font, text=f"The result of the computation was: \n{results[locToFind][0]}", text_color=textColor)
            display_computation_result.pack(padx=20, pady=20)
        elif locToFind == "Percentiles":
            display_computation_result = customtkinter.CTkLabel(self, font=font, text=f"The result of the computation was: \n{results[locToFind][0]}", text_color=textColor)
            display_computation_result.pack(padx=20, pady=20)

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
        
        array_data =  [float(x) for x in data] 
        sorted_data = sorted(array_data)
        
        Q1, flag1 = ComputeQuartile(data=sorted_data, k="1") 
        Q2, flag2 = ComputeQuartile(data=sorted_data, k="2")
        Q3, flag3 = ComputeQuartile(data=sorted_data, k="3")

        results["Quartiles"].clear()
        if flag1 == True:
            results["Quartiles"].append((Q1, Q1))
        else: 
            results["Quartiles"].append((round(Q1), Q1))
        if flag2 == True:
            results["Quartiles"].append((Q2, Q2))
        else:
            results["Quartiles"].append((round(Q2), Q2))
        if flag3 == True:
            results["Quartiles"].append((Q3, Q3))
        else:
            results["Quartiles"].append((round(Q3), Q3))
        


        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = InputWindow("Quartiles")  
        else:
            self.toplevel_window.focus()

    def calculatePercentile(self):
        global entries, results
        array_data =  [float(x) for x in data] 
        sorted_data = sorted(array_data)
        


        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = InputWindow("Percentiles")  
        else:
            self.toplevel_window.focus()

    def calculateDecile(self):
        global entries, results
        array_data =  [float(x) for x in data] 
        sorted_data = sorted(array_data)


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
        self.title("Measures of Location Calculator")
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