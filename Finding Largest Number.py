
"""Finding Large Number"""

Num1 = int(input("Enter Number 1:"))

Num2 = int(input("Enter Number 2:"))

Num3 = int(input("Enter Number 3:"))



if (Num1 < Num2) and (Num1 < Num3):
    Largest = Num1
if (Num2 < Num1) and (Num2 < Num3):
    Largest = Num2
else:
    Largest = Num3

print("Largest Number is",Largest)    

