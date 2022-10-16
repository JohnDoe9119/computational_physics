# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:39:39 2022

@author: Chris
"""

from pylab import*


Xmin = -5.0;        Xmax = 5.0;         Npoints = 500
#mathematical functions for the plotting
DelX =(Xmax-Xmin)/Npoints
x1 = arange(Xmin, Xmax, DelX)
x2 = arange(Xmin, Xmax, DelX/20)            #Different x2 range
y1 = -sin(x1)*cos(x1*x1)                    #Function 1 
y2 = exp(-x2/4.)*sin(x2)                    #Function 2
print("\n Now plotting . look for Figures 1 & 2 on Desktop")

figure(1)               #creating the first figure
subplot(2,2,1)          #1st subplot in first figure
#subplot(nrow, ncol, index)
plot(x1, y1, 'r', lw= 2)
xlabel('x');     ylabel('f(x)');     title('$-\sin(x)*\cos(x^2)$')
grid(True, ls=':')
subplot(2,2,3)          #2nd subplot in first figure
plot(x2, y2, '-', lw= 2)
xlabel('x')
ylabel('f(x)')
title('exp(-x/4)*\sin(x)')
#figure(2)              #comented out to put all in one figure
subplot(2,2,2)          #1st subplot in 2nd figure
plot(x1, y1*y1, 'r', lw= 2)
xlabel('x'); ylabel('f(x)'); title('$-\sin^2(x)*\cos^2(x^2)$')

    #form grid
subplot(2,2,4)          #2nd subplot in 2nd figure
plot(x2, y2*y2, '-', lw= 2)
xlabel('x'); ylabel('f(x)'); title('$\exp(-x/2)*\sin^2(x)$')
grid(True, ls=':')
subplots_adjust(wspace=.3,hspace=.8) #adjusting width and heightspace btw. subplots
show()