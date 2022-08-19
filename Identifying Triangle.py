"""Cheacking Triangle"""

x = int(input("x :"))

y = int(input("y :"))

z = int(input("z :"))

if x == y == z:
    input("Equilateral Triangle")
    
if x==y or y==z or z==x:
    input("Isosceles Triangle")

else:
    input("Scalene Triangle")
     