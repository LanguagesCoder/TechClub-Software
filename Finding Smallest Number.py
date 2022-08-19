# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:18:58 2020

@author: sir
"""

Num1 = int(input("Enter Number 1:"))

Num2 = int(input("Enter Number 2:"))

Num3 = int(input("Enter Number 3:"))

Num4 = int(input("Enter Number 4:"))

Num5 = int(input("Enter Number 5:"))

Num6 = int(input("Enter Number 6:"))

Num7 = int(input("Enter Number 7:"))

Num8 = int(input("Enter Number 8:"))

num_list=[Num1,Num2,Num3,Num4,Num5,Num6,Num7,Num8]
print(num_list)

if (Num1 > Num2) and (Num1 > Num3):
    Smallest = Num1
if (Num2 > Num1) and (Num2 > Num3):
    Smallest = Num2
if (Num3 > Num4) and (Num3 > Num5):
    Smallest = Num3
if (Num4 > Num3) and (Num4 > Num5):
    Smallest = Num4
if (Num5 > Num6) and (Num5 > Num7):
    Smallest = Num5
if (Num6 > Num5) and (Num6 > Num7):
    Smallest = Num6
if (Num7 > Num6) and (Num7 > Num8):
    Smallest = Num7
else:
    Smallest = Num8
    
print("Smallest Number is",Smallest)    

    