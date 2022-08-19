# Advanced Datatype
"""
Advanced Datatypes
Question Game 
"""

Questions = ["1.What is the Capital Of Japan?","2.Who is the first Prime Minister of India","3.What is the full name of Mahatma Gandhi?"]

Answers = ["Tokyo","Jawaharlal Nehru","Mohandas Karamchand Gandhi"]   

Score = 0

for x in range(3):
    
    print(Questions[x])
    ans = input("Whats Your Answer ? Please Enter:")


    if ans == Answers[x]:
        print("Correct Answer!")
        Score = Score + 2
        print(" ")
        print("Your Score is "+str(Score))
        print(" ")
    else:
        print("Wrong Answer!")
        Score = Score - 0
        print(" ")
        print("Your Score is "+str(Score))
        print(" ")
        
print("Your Total Score is "+str(Score))    
    
if Score == 6:
    print("Genius")
elif Score == 4:
    print("Fantastic")
else:
    print("You Need to Improve Your General Knowledge")    
                                    