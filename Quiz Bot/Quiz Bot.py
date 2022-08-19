""" Program for Quizbot """

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
            else:
                print ("Wrong Answer")
                print (Score)
  
    
    
    
    
    
    
        if Qnum==2:
            
            print ("Corona Virus patient was firstly in which country ?")
            print ("Options A:India B:Britain C:Russia D:China")
            
            ans = input ("Whats your answer?:")
            
            if ans == 'd' or ans =='D':
                print ("Correct Answer")
                Score=Score+1
                print(Score)
            else:
                print ("Wrong Answer")
                print (Score) 
                
                
                
                
                
                
                
                
                
        if Qnum==3:
            
            print ("Who is the Recent President of USA ?")
            print ("Options A:Narendra Modi B:Donald Trump C:Xi Jinping D:Putin")
            
            ans = input ("Whats your answer?:")
            
            if ans == 'b' or ans =='B':
                print ("Correct Answer")
                Score=Score+1
                print(Score)
            else:
                print ("Wrong Answer")
                print (Score)         
                
                
                
                
                
                
        if Qnum==4:
            
            print ("What is the formule of water ?")
            print ("Options A:Co2 B:O2 C:H2O D:HO2")
            
            ans = input ("Whats your answer?:")
            if ans == 'c' or ans =='C':
                print ("Correct Answer")
                Score=Score+1
                print(Score)
            else:
                print ("Wrong Answer")
                print (Score)                 
                
                
                
                
                
        if Qnum==5:
            
            print ("Who is called father of nation ?")
            print ("Options A:Mahatma Gandhi B:Karl Marx C:Scorates D:Abraham lincoln")
            
            ans = input ("Whats your answer?:")
            if ans == 'a' or ans =='A':
                print ("Correct Answer")
                Score=Score+1
                print(Score)
            else:
                print ("Wrong Answer")
                print (Score)                   
                
                
                
                
                
        Qnum = Qnum + 1    
        
        if Score == 5:
           print("You are a Genius!!!") 
                
print ("Thanks for playing")
print ("We are Out")                
                
                
                
                
                
                
                
                
                
                
                
                
                
                