# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:01:32 2020

@author: sir
"""
guess = 50
import random
n = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))
while n != "guess":
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("you guessed it!")
        break