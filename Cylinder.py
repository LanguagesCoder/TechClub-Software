# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:31:07 2020

@author: sir
"""

pi=22/7
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))
Volume = pi * radian * radian * height
area = ((2*pi*radian) * height) + ((pi*radian**2)*2)
Perimeter = height + radian
print("Volume is: " +str(Volume))
print(" Area is: " +str(area))
print("Perimeter is:" +str(Perimeter))