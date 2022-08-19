import time
import datetime

cnum=input("Enter your card number:")
time.sleep(0.10)
if cnum=="44892":
    time.sleep(4)
    print("Cheacking Validity")
    tday=datetime.date.today()
    expday=datetime.date(2019,3,1)
    time.sleep(2)
    print("Expiry date i"+str(expday))
    print("Todays date"+str(tday))
    time.sleep(2)
    if tday>expday :
        print("Your card is invalid")
        
    else :
        print("Your card is valid")
        
if cnum=="11025":
    time.sleep(4)
    print("Cheacking Validity")
    tday=datetime.datetime.today()
    expday=datetime.date(2020,3,1)
    time.sleep(2)
    print("Expiry date i"+str(expday))
    print("Todays date"+str(tday))
    time.sleep(2)
    if tday>expday :
        print("Your card is invalid")
        
    else :
        print("Your card is valid")
       
        
if cnum=="22686" :
    time.sleep(4)
    print("Cheacking Validity")
    tday=datetime.datetime.today() 
    expday=datetime.datetime(2020,4,1,17,5,0,00)
    time.sleep(2)
    print("Expiry date i"+str(expday))
    print("Todays date"+str(tday))
    time.sleep(2)
    if tday>expday :
        print("Your card is invalid")
        
    else :
        print("Your card is valid")
       

if cnum=="45226":
    time.sleep(4)
    print("Cheacking Validity")
    tday=datetime.date.today()
    expday=datetime.date(2020,4,1)
    time.sleep(2)
    print("Expiry date"+str(expday))
    print("Todays date"+str(tday))
    time.sleep(2)
    if tday>expday :
        print("Your card is invalid")
        
    else :
        print("Your card is valid")
        