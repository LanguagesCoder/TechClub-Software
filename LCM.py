# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:05:23 2020

@author: sir
"""
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter the first Number :"))
num2 = int(input("Enter the second Number :"))

print("The L.C.M. is", compute_lcm(num1, num2))
  