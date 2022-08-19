#Eng = English
#Ma = Maths
#Es = E.V.S
#St = SSt
#Mar = Marathi
Marks = 0

print("Eng stands for English")
print(" ")
print("Ma stands for Maths")
print(" ")
print("Es stands for E.V.S")
print(" ")
print("St stands for Sst")
print(" ")
print("Mar stands for Marathi")
print(" ")
print("All the paper were of 80 marks")
print(" ")
print("The total Marks are 400")

Eng = int(input("Please enter the marks of English:"))

Ma = int(input("Please enter the marks of Maths:"))

Es = int(input("Please enter the marks of E.V.S:"))

St = int(input("Please enter the marks of Sst:"))

Mar = int(input("Please enter the marks of Marathi:"))
 
Marks = Eng + Ma + Es + St + Mar

print("You got 400 out of"+str(Marks))

