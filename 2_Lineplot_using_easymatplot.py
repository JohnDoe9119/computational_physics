# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 23:01:02 2022

@author: Chris
"""
from matplotlib.pylab import *
Xmin = -5.; Xmax= +5.;Npoints=500
DelX = (Xmax- Xmin)/Npoints
x = arange(Xmin, Xmax, DelX)
y = sin(x) * sin(x*x)
#print('arange => x[0], x[1], x[499]= %8.2f %8,2f %8.2f'
#      %(x[0],y[1],x[499]))
#print('arange => y[0], y[1], y[499]= %8.2f %8,2f %8.2f'
#      %(x[0],y[1],x[499]))
print("\n Doing plotting, look for figure 1" )
xlabel('x'); ylabel('f(x)'); title('f(x) vs x')
text(-1.75, 0.75,'MatPlotLib \n Example')
plot(x,y, '-', lw=2)                            #'-' is indicating the usage of a line
grid(True)
show()
#=================