





"""Program For Ice Cream Parlor"""


price=0
done=0

print("Welcome to the 'great Ice Cream Shop'")
print("choose your flavour")
print("1.Mango          75/-")
print("2.Choco Chips    95/-")
print("3.Black Current  80/-")
print("4.Blue Berry     100/-")

while done==0:
    Choice  =  int(input("Enter Your Choice!:"))

    if Choice==1: 
        price = price+75
    elif Choice==2:
        price = price+95
    if Choice==3:
        price = price+80
    elif Choice==4:
        price = price+100
    else:
        print("Thank u!")
        

    more = input ("Good Choice!Would you like to buy more?")

    if more =="Yes" or more =="yes":
         done = 0
    else:
         done = 1
         print("\nThanks for the purchase. \nYour bill is : Rs "+ str(price))




