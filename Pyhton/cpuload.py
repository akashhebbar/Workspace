import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg 
import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import numpy as np
from tkinter import *

class window():
def __init__(self):
    self.root = Tk()


    self.canvas = Canvas(self.root)
    self.canvas.pack()

    self.figure = Figure(figsize=(5,5),dpi=100)
    self.plot1 = self.figure.add_subplot(111)
    self.plot1.set_title("Plot1")
    self.plot1.set_ylabel("Werte")
    self.plot1.set_xlabel("X-Werte")
    self.x = np.array([1,2,3,4,5,6,7,8,9,10])
    self.y = self.x**2
    self.plot1.plot(self.x,self.y)

    self.Graph_canvas = FigureCanvasTkAgg(self.figure,self.canvas)
    #self.Graph_canvas.show()
    self.Graph_canvas.get_tk_widget().pack()

    self.Toolbar = NavigationToolbar2TkAgg(self.Graph_canvas,self.root)
    #self.Toolbar.update()
    self.Toolbar.pack()