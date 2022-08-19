import time

LoginDetails={"durgesh":"mypaswd47744!",
              "hemant":"hemantpas445*",
              "leena":"tutuions",
              "kavate":"Kavatesus"}

username=input("Enter your UserName: ")
print("Processing")
time.sleep(10)
paswd=input("Enter Password: ")
time.sleep(10)
print("Cheacking")

if username in LoginDetails.keys():
    time.sleep(4)
    if LoginDetails[username]==paswd:
        print("Authenticated!!")
    else:
        print("Invalid Password!!")
        
else:
    print("Invalid Username!!")

    

    