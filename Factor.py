# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:04:40 2020

@author: sir
"""

# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter the number for the factor :"))

print_factors(num)
