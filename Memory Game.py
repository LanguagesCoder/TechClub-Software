import time

numList=[12,300,67,45,78]
userList=[0,0,0,0,0]

score=0

print("Memorize the sequence!!")
time.sleep(1)

for i in numList:
    print(i)
    time.sleep(1)
    
time.sleep(3)

for x in range(202):
    print("||")
    
for y in range(5):
    
    userList[y]=int(input("Number " + str(y+1)+" : "))
    if userList[y]==numList[y]:
        score=score+1
    
        
if score<=2:
    print("You need Almonds Man!!")
    
    
elif score<=4:
    print("You need to improve")
else:
    print("You have sharp Memory!!")
   
print("Your Score is: " + str(score))