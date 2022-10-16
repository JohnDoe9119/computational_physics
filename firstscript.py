# -*- coding: utf-8 -*-
import matplotlib as plt
from vpython import *
"""
Created on Mon Oct 10 21:53:23 2022

@author: Chris
"""
graph1=graph(align='left', width=400, height=400,
             background=color.white, foreground=color.black)
Plot1=gcurve(color=color.red)
for x in arange(0, 8.1,0.1):
    Plot1.plot(pos=(x,5*cos(2*x)*exp(-0.4*x)))
graph2=graph(align='right', width=400, height=400,
             background=color.white, foreground=color.black,
             title='2-D Plot', xtitle='x',ytitle='f(x)')
Plot2=gdots(color=color.black)
for x in arange(-5,5,0.1):
    Plot2.plot(pos=(x,cos(x)))
#=================Now 3GraphVP script
#also uses vpython import*
string="blue: sin^2(x), black= cos^2(x), cyan: sin(x)*cos(x)"
graph3=graph(title=string, xtitle="x", ytitle="y",
             background=color.white, foreground=color.black)
y1 = gcurve(color=color.blue)
y2 = gvbars(color=color.black)
y3 = gdots(color=color.cyan)
for x in arange(-5,5,0.1):
    y1.plot(pos=(x,sin(x)**2))
    y2.plot(pos=(x, cos(x)*cos(x)/3.))
    y3.plot(pos=(x, sin(x)*cos(x)))
