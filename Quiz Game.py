# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:23:42 2020

@author: sir
"""

score = 0
count = 0

while count<=3:
    if count == 1:
        print("What is Capital of Maharashtra?")
        ans = input("A:Delhi B:Calcutta C:Mumbai").lower()
        if ans == "c":
            score = score = 1
            print("Correct Answer ! Your Score"+str(score))
        else:
            score = score - 1
            print("wrong Answer!Your Score"+str(score))
            
    if count == 2:
        print("What is Covid 19?")
        ans = input("A:Bacteria B:Fungus C:Virus").lower()
        if ans == "c":
            score = score = 1
            print("Correct Answer ! Your Score"+str(score))
        else:
            score = score - 1
            print("wrong Answer!Your Score"+str(score))
            
    if count == 1:
        print("What is Square of 3?")
        ans = input("A:12 B:6 C:9").lower()
        if ans == "c":
            score = score = 1
            print("Correct Answer ! Your Score"+str(score))
        else:
            score = score - 1
            print("wrong Answer!Your Score"+str(score))
            
            
print("Game Over")
print("Your Score"+str(score))            
            