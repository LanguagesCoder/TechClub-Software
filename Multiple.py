# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:07:00 2020

@author: sir
"""


# function to print the first m multiple 
# of a number n without using loop. 
def multiple(m, n): 
  
    # inserts all elements from n to  
    # (m * n)+1 incremented by n. 
    a = range(n, (m * n)+1, n) 
      
    print(*a) 
  
# driver code  
m = int(input("Enter the Value of m:"))
n = int(input("Enter the Value of n:"))
multiple(m, n)