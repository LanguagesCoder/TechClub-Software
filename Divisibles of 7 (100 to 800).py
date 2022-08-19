lower=int(input("Enter the lower range: "))
upper=int(input("Enter the upper range: "))
for num in range(lower,upper+1):
    if (num %7) == 0:
        print(num)
              
              