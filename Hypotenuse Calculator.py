# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:08:11 2020

@author: sir
"""
while " ":
    using = input("Do you want to use the calculator for hypotenuse of triangle:")
    if using == "Yes":
        print("Input lengths of shorter triangle sides:")
        a = float(input("a: "))
        b = float(input("b: "))

        hypotenuse = (a**2 + b**2)
        print("The length of the hypotenuse is", hypotenuse )
        
    else:
         print("Thank You")
         break