#!/usr/bin/env python3

import pylab as pl
from pylab import linspace, pi, plot, sin, cos, show


def fceSoubor():
    cesta = souborVar.get()
    f = open(cesta,'r')
    x=[]
    y=[]
    while 1:
        radek=f.readline()
        if radek=='':
            break
        cisla=radek.split()
        x.append( float(cisla[0]) )
        y.append( float(cisla[1]) )
        f.close()
        pl.figure()
        pl.plot(x,y)
        pl.xlabel(osaxVar.get())
        pl.ylabel(osayVar.get())
        pl.grid(True)
        pl.show()
    