import tkinter as tk
from MainScreen import *

class Parametrs:
    def __init__(self, pop, S1, S2, S3, S4, l, mode):
        self.population = pop
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
        self.S4 = S4
        self.L = l
        self.mode = mode

params = Parametrs("80", "25", "25", "25", "25", "5", False)

class ParamScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg="#dbd6c3")
        tk.Label(self, text="PARAMETERS", bg="#dbd6c3", font=("Calibri", 24)).pack(pady=15)
        self.labelPop = tk.Label(self, text="POPULATION DENSITY:", bg="#dbd6c3", font=("Calibri", 12)).pack(pady=5)
        self.entryPop = tk.Entry(self, validate="key")
        self.entryPop['validatecommand'] = (self.entryPop.register(self.validate_entry), '%P')
        self.entryPop.pack()
        self.labelS1 = tk.Label(self, text="S1:", bg="#dbd6c3", font=("Calibri", 12)).pack(pady=5)
        self.entryS1 = tk.Entry(self, validate="key")
        self.entryS1['validatecommand'] = (self.entryS1.register(self.validate_entry), '%P')
        self.entryS1.pack()
        self.labelS2 = tk.Label(self, text="S2:", bg="#dbd6c3", font=("Calibri", 12)).pack(pady=5)
        self.entryS2 = tk.Entry(self, validate="key")
        self.entryS2['validatecommand'] = (self.entryS2.register(self.validate_entry), '%P')
        self.entryS2.pack()
        self.labelS3 = tk.Label(self, text="S3:", bg="#dbd6c3", font=("Calibri", 12)).pack(pady=5)
        self.entryS3 = tk.Entry(self, validate="key")
        self.entryS3['validatecommand'] = (self.entryS3.register(self.validate_entry), '%P')
        self.entryS3.pack()
        self.labelS4 = tk.Label(self, text="S4:", bg="#dbd6c3", font=("Calibri", 12)).pack(pady=5)
        self.entryS4 = tk.Entry(self, validate="key")
        self.entryS4['validatecommand'] = (self.entryS4.register(self.validate_entry), '%P')
        self.entryS4.pack()
        self.labelL = tk.Label(self, text="L:", bg="#dbd6c3", font=("Calibri", 12)).pack(pady=5)
        self.entryL = tk.Entry(self, validate="key")
        self.entryL['validatecommand'] = (self.entryL.register(self.validate_entry2), '%P')
        self.entryL.pack()
        self.toggle_state = tk.BooleanVar()
        self.toggle_button = tk.Checkbutton(self, text="STRATEGIC MODE", bg="#dbd6c3", font=("Calibri", 10),variable=self.toggle_state,onvalue=True,offvalue=False)
        self.toggle_button.pack(pady=25)
        self.labelNotValid = tk.Label(self, text="", fg="red" , bg="#dbd6c3", font=("Calibri", 12))
        self.labelNotValid.pack(pady=10)
        tk.Button(self, text="START", font=("Calibri", 12), command=self.goto_main_screen, borderwidth = '4', bg='#236b37', relief="groove",padx=7, pady=3).pack()

    def validate_entry(self, text):
        # Only allow integers between 0 and 100
        if text == "":
            return True
        if text.isdigit():
            num = int(text)
            if num >= 0 and num <= 100:
                return True
        return False

    def validate_entry2(self, text):
        # Only allow integers between 0 and 50
        if text == "":
            return True
        if text.isdigit():
            num = int(text)
            if num >= 0 and num <= 50:
                return True
        return False

    def validate_not_empty(self):
        if (
                params.population != "" and params.S1 != "" and params.S2 != "" and params.S3 != "" and params.S4 != "" and params.L != ""):
            return True
        return False

    def validate_S(self):
        if (int(params.S1) + int(params.S2) + int(params.S3) + int(params.S4) != 100):
            self.labelNotValid.config(text="S1+S2+S3+S4 != 100")
            return False
        return True

    def goto_main_screen(self):
        params.population = self.entryPop.get()
        params.S1 = self.entryS1.get()
        params.S2 = self.entryS2.get()
        params.S3 = self.entryS3.get()
        params.S4 = self.entryS4.get()
        params.L = self.entryL.get()
        params.mode = self.toggle_state.get()
        if self.validate_not_empty():
            if self.validate_S():
                self.master.switch_frame(MainScreen)