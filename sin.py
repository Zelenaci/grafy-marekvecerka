from tkinter import *
import pylab as pl
from pylab import linspace, pi, plot, sin, cos, show
import numpy as np

okno = Tk()
okno.config(padx=10,pady=10)
okno.title("Graf Cos")

fcePerioda=StringVar()
fceFrekvence=StringVar()
fceAmplituda=StringVar()
fcePosun=StringVar()

fcePerioda.set("Periody")
fceFrekvence.set("Frekvence")
fceAmplituda.set("Amplituda")
fcePosun.set("Fázový posun")

fceFrame=LabelFrame(okno, text="Parametry", padx=5, pady=5)
fceFrame.grid(column=0,row=0, sticky=W+E)
fceFrame.grid_columnconfigure(1,weight=1)

Entry(fceFrame, textvariable=fcePerioda, width=11).grid(column=1, row=1, sticky=E)
Entry(fceFrame, textvariable=fceFrekvence, width=11).grid(column=1,row=2, sticky=E)
Entry(fceFrame, textvariable=fceAmplituda, width=11).grid(column=1, row=3, sticky=E)
Entry(fceFrame, textvariable=fcePosun, width=11).grid(column=1, row=4, sticky=E)

def cosGraf():
    try:    
        perioda=float( fcePerioda.get())
        frekvence=float( fceFrekvence.get())
        amplituda=float( fceAmplituda.get())
        faz_posun=float( fcePosun.get())
        x=pl.linspace(0, periody*1/frekvence, frekvence*10000)
        y=amplituda * (np.sin(2*pi*frekvence*x + np.deg2rad(faz_posun)))

        pl.plot(x,y, label="Graf Cos")
        pl.xlabel("t[s]")
        pl.ylabel("U[V] | I[A] | P[W]")
        pl.grid(True)
        pl.show()
    except:
        pass


Button(okno, text="Vytvoř graf",command=cosGraf).grid(column=1,row=0, sticky=W+E+N+S)


okno.mainloop()