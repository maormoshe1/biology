
import tkinter as tk
from ParameterScreen import *
from MainScreen import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("800x800")
        self.configure(bg="#dbd6c3")
        self._frame = None
        self.switch_frame(ParamScreen)
        #self.switch_frame(MainScreen)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

app = App()
app.mainloop()


