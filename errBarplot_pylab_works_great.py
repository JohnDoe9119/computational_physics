# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:21:23 2022

@author: Chris
"""
import matplotlib.pylab as p
from numpy import*

p.title('Grade Inflation')
p.xlabel('Years in College')
p.ylabel('GPA')
xa = array([-1, 5])
ya = array([0, 0])
x0 = array([0, 1, 2, 3, 4])
y0 = array([-1.4, +1.1, 2.2, 3.3, 4.0])
p.plot(xa,ya) #this makes a horizontal line Axis?
p.plot(x0,y0,'bo')  #dataset 0 blue circles
p.plot(x0,y0,'g')   #data set 0 line
x1 = arange(0, 5, 1) # Data set 1 points
y1 = array([4.0,2.7, -1.8, 0.9, 2.6])
p.plot(x1, y1, 'r')
errTop = array([1.0, 0.3, 1.2, 0.4, 0.1])
errBot = array([2.0, 0.6, 2.3, 1.8, 0.4])
p.errorbar(x1,y1, [errBot, errTop], fmt ='o') #plot errorbars


p.grid(True)
p.show()