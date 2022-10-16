# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:25:20 2022

@author: Chris
"""
#PondMatPlot . py : Monte−Carlo integration via von Neumann  - rejection
#Numerische Integration einer Funktion mittels Zufallszahlen

import numpy as np
import matplotlib.pyplot as plt

N, Npts = 1000, 5000;
analyt = np.pi**2           #analytic solution
x1 = np.arange(0, 2*np.pi+2*np.pi/N , 2*np.pi/N)
xi= []; yi = []; xo = []; yo=[]
fig, ax = plt.subplots()
y1 = x1 * np.sin(x1)**2                 #Integrand visualization
ax.plot(x1, y1, 'c', lw=4)
ax.set_xlim((0,2*np.pi))
ax.set_ylim((0, 5)) 
ax.set_xticks([0, np.pi, 2*np.pi])
ax.set_xticklabels(['0','$\pi$','2$\pi$']) #mathprint xaxis ticks
ax.set_ylabel('$f(x) = x\,\sin^2 x$', fontsize =20)
ax.set_xlabel('x', fontsize = 20)
fig.patch.set_visible(True)

def fx(x):  return x*np.sin(x)**2       #Integrand

j = 0                                   #inside curve counter
xx = 2.*np.pi * np.random.rand(Npts)    #0=< x <= 2pi
yy = 5*np.random.rand(Npts)             #0=< y <= 5
boxarea = 2.*np.pi * 5                  #Box area
for i in range(1,Npts):
    #plt.pause(0.000001)
    if (yy[i]<= fx(xx[i])):
        xi.append(xx[i])
        yi.append(yy[i])
        j +=1
    else:
        yo.append(yy[i])
        xo.append(xx[i])
        
    area = boxarea*j/(Npts-1)           #Area under curve
    #The ratio of “hits” to total number of stones thrown 
    #equals the ratio of the area of the pond tothat of the box.
ax.plot(xo,yo,'bo', markersize = 1)
ax.plot(xi,yi,'ro',markersize = 1)
ax.set_title('Answer: Analytic = %5.3f, MonteCarlo Integr.= %5.3f' %(analyt, area))
plt.show()
print('Answer: Analytic = %5.3f, MC= %5.3f' %(analyt, area))
    