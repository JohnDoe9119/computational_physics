# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:16:47 2022

@author: Chris
"""
import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axes3D
#plot is rotatable and scaleable in pycharm but not spider

print('Please be patient while I do importing & plotting')
delta=.1
x = p.arange( -3,3,delta)
y = p.arange( -3,3,delta)
X, Y = p.meshgrid(x,y)
Z = p.sin(X)* p.cos(Y)          #Surface height
fig = p.figure()
ax= Axes3D(fig)
ax.plot_surface(X,Y,Z)
ax.plot_wireframe(X,Y,Z, color ='r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
p.show()