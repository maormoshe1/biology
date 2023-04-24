
import tkinter as tk
from ParameterScreen import *
from MainScreen import *
import matplotlib.pyplot as plt

avgRed = [0 for i in range(41)]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("800x800")
        self._frame = None
        #self.switch_frame(ParamScreen)
        self.switch_frame(MainScreen)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

app = App()
app.mainloop()
#
# for i in range(3):
#     app = App()
#     app.mainloop()
#     for r in range(41):
#         avgRed[r] = (avgRed[r]*i + reds[r])/(i+1)
#     reds.clear()
#
# generations = [i for i in range(41)]
#
# # plotting the points
# plt.plot(generations, avgRed)
#
# # naming the x axis
# plt.xlabel('x - generations')
# # naming the y axis
# plt.ylabel('y - knows the rumor')
#
# # function to show the plot
# plt.show()


