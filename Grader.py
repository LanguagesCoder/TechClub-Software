English=float(input("Enter marks of the English:"))
Maths=float(input("Enter marks of the Maths:"))
Evs=float(input("Enter marks of the Evs:"))
SSt=float(input("Enter marks of the SSt:"))
Marathi=float(input("Enter marks of the Marathi:"))
Total = (English + Maths + Evs + SSt + Marathi)
print(Total)
TotalLoss = (500 - Total)
print(TotalLoss)
Percentage=Total / 500 * 100
print(Percentage)
if(Percentage>=90):
    print("Distinction")
elif(Percentage>=80 and Percentage<90):
    print("Rank:1")
elif(Percentage>=70 and Percentage<80):
    print("Rank:2")
elif(Percentage>=60 and Percentage<70):
    print("Rank:3")
else:
    print("Fail")    
    
        