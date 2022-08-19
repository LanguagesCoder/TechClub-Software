""" Program for Quizbot """
import time 
import pygital_v2 as Bot


Bot.pinMode (2,"dOutput")
Bot.pinMode (3,"dOutput")
Bot.pinMode (4,"dOutput")
Bot.pinMode (5,"dOutput")
Bot.pinMode (6,"dOutput")

Bot.init("COM7")
Qnum=1
Score=0

while Qnum<=5:
    
    
    
    
        if Qnum==1:
            
            print ("Which is the national animal of India?")
            print ("Options A:Tiger B:Lion C:Monkey D:Deer")
            
            ans = input ("Whats your answer?:")
            
            if ans == 'a' or ans =='A':
                print ("Correct Answer")
                Score=Score+1
                print(Score)
                Bot.dwrite(2,1)
            else:
                print ("Wrong Answer")
                print (Score)
                Bot.dwrite(2,0)
    
    
    
    
    
    
        if Qnum==2:
            
            print ("Corona Virus patient was firstly in which country ?")
            print ("Options A:India B:Britain C:Russia D:China")
            
            ans = input ("Whats your answer?:")
            
            if ans == 'd' or ans =='D':
                print ("Correct Answer")
                Score=Score+1
                print(Score)
                Bot.dwrite(3,1)
            else:
                print ("Wrong Answer")
                print (Score) 
                Bot.dwrite(3,0)
                
                
                
                
                
                
                
                
        if Qnum==3:
            
            print ("Who is the Recent President of USA ?")
            print ("Options A:Narendra Modi B:Donald Trump C:Xi Jinping D:Putin")
            
            ans = input ("Whats your answer?:")
            
            if ans == 'b' or ans =='B':
                print ("Correct Answer")
                Score=Score+1
                print(Score)
                Bot.dwrite(4,1)
            else:
                print ("Wrong Answer")
                print (Score)         
                Bot.dwrite(4,0)
                
                
                
                
                
        if Qnum==4:
            
            print ("What is the formule of water ?")
            print ("Options A:Co2 B:O2 C:H2O D:HO2")
            
            ans = input ("Whats your answer?:")
            if ans == 'c' or ans =='C':
                print ("Correct Answer")
                Score=Score+1
                print(Score)
                Bot.dwrite(5,1)
            else:
                print ("Wrong Answer")
                print (Score)                 
                Bot.dwrite(5,0)
                
                
                
                
        if Qnum==5:
            
            print ("Who is called father of nation ?")
            print ("Options A:Mahatma Gandhi B:Karl Marx C:Scorates D:Abraham lincoln")
            
            ans = input ("Whats your answer?:")
            if ans == 'a' or ans =='A':
                print ("Correct Answer")
                Score=Score+1
                print(Score)
                Bot.dwrite(6,1)
            else:
                print ("Wrong Answer")
                print (Score)  
                Bot.dwrite(6,0)                 
                
                
                
                
                
        Qnum = Qnum + 1    
        
        if Score == 5:
           print("You are a Genius!!!") 
                
print ("Thanks for playing")
print ("We are Out")                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

