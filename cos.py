
import pylab as pl
import tkinter as tk

from pylab import linspace,pi,plot,cos,show
from os.path import basename,splitext
from tkinter import *



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Graf Cos"

    def __init__(self):

        super().__init__(className=self.name)

        self.title(self.name)
        self.lbl = tk.Label(self, text="Graf Cos")
        self.lbl.pack()

        
        self.var_entryPerioda = tk.IntVar()
        self.var_entryFrekvence = tk.IntVar()
        self.var_entryAmplituda = tk.IntVar()  
        
        #zadání periody
        self.lbl2 = tk.Label(self, text="Počet period")
        self.lbl2.pack()
        self.entryPerioda  = tk.Entry(self, textvariable = self.var_entryPerioda)
        self.entryPerioda.pack()
        #zadání frekvence
        self.lbl3 = tk.Label(self, text="Frekvence")
        self.lbl3.pack()
        self.entryFrekvence  = tk.Entry(self, textvariable = self.var_entryFrekvence)
        self.entryFrekvence.pack()
        #zadání amplitudy
        self.lbl4 = tk.Label(self, text="Amplituda")
        self.lbl4.pack()
        self.entryAmplituda  = tk.Entry(self, textvariable = self.var_entryAmplituda)
        self.entryAmplituda.pack()


        self.btnGraf = tk.Button(self, text="Vytvoř graf", command=self.graf)
        self.btnGraf.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        
    def quit(self, event=None):
        super().quit()
    
    def graf(self):
        self.f = self.var_entryFrekvence.get()
        self.a = self.var_entryAmplituda.get()
        self.p = self.var_entryPerioda.get()
        x = pl.linspace(0, self.p/self.f, self.f*10000)
        y = self.a * (pl.cos(2*pi*self.f*x ))
        pl.plot(x,y)
        pl.title("Graf cos")
        pl.xlabel("t[s]")
        pl.ylabel("U[V],I[A],P[W]")
        pl.show()


app = Application()
app.mainloop()