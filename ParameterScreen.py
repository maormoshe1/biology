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

params = Parametrs("80", "25", "25", "25", "25", "2", False)

class ParamScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="Parameters", font=("Arial", 24)).pack()
        self.labelPop = tk.Label(self, text="Population Density:", font=("Arial", 12)).pack()
        self.entryPop = tk.Entry(self, validate="key")
        self.entryPop['validatecommand'] = (self.entryPop.register(self.validate_entry), '%P')
        self.entryPop.pack()
        self.labelS1 = tk.Label(self, text="S1:", font=("Arial", 12)).pack()
        self.entryS1 = tk.Entry(self, validate="key")
        self.entryS1['validatecommand'] = (self.entryS1.register(self.validate_entry), '%P')
        self.entryS1.pack()
        self.labelS2 = tk.Label(self, text="S2:", font=("Arial", 12)).pack()
        self.entryS2 = tk.Entry(self, validate="key")
        self.entryS2['validatecommand'] = (self.entryS2.register(self.validate_entry), '%P')
        self.entryS2.pack()
        self.labelS3 = tk.Label(self, text="S3:", font=("Arial", 12)).pack()
        self.entryS3 = tk.Entry(self, validate="key")
        self.entryS3['validatecommand'] = (self.entryS3.register(self.validate_entry), '%P')
        self.entryS3.pack()
        self.labelS4 = tk.Label(self, text="S4:", font=("Arial", 12)).pack()
        self.entryS4 = tk.Entry(self, validate="key")
        self.entryS4['validatecommand'] = (self.entryS4.register(self.validate_entry), '%P')
        self.entryS4.pack()
        self.labelL = tk.Label(self, text="L:", font=("Arial", 12)).pack()
        self.entryL = tk.Entry(self, validate="key")
        self.entryL['validatecommand'] = (self.entryL.register(self.validate_entry2), '%P')
        self.entryL.pack()
        self.toggle_state = tk.BooleanVar()
        self.toggle_button = tk.Checkbutton(self, text="astrategic mode",font=("Helvetica", 10),variable=self.toggle_state,onvalue=True,offvalue=False)
        self.toggle_button.pack()
        self.labelNotValid = tk.Label(self, text="", fg="red" , font=("Arial", 12))
        self.labelNotValid.pack(pady=10)
        tk.Button(self, text="Start", font=("Helvetica", 16), command=self.goto_main_screen, bg='blue', padx=10, pady=5).pack(pady=25)

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