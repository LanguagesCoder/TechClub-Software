import pyttsx3 


"""
Global Variables
"""
todo = ''
engine = pyttsx3.init() 
msg_list = ['Calculating Area', 
            'Calculating Perimeter',
            'Calculating Volume'
             ]
"""
Function Definitions
"""

def speech_init():
    
    engine.setProperty('rate', 125)
    engine.setProperty('volume',100) 
    
    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[0].id)   

def speakOut(msg):
    engine.say(msg)
    engine.runAndWait()
    
def area(length,breadth):
    cal_area=  length * breadth    
    print("Area of Rectangle is :" + str(cal_area)) 
    speakOut("Area of Rectangle is :" + str(cal_area))
    pass

def perimeter(length, breadth):
    cal_peri = 2*(length+breadth)
    print("Perimeter of Rectangle is :" + str(cal_peri))
    speakOut("Perimeter of Rectangle is :" + str(cal_peri))
    pass
    
def volume(length,breadth,height):
    cal_vol = length * breadth * height
    print("Volume of Rectangle is :" + str(cal_vol))
    speakOut("Volume of Rectangle is :" + str(cal_vol))
    pass
    
def UI():
    print("Welcome to the Calculator!")
    speakOut("Welcome to the Calculator!")
    print("I can help you calculate 1. Area 2.Perimeter 3. Volume 4.Exit")
    option = input('Enter your choice : ')
    return option 
def decode(option):
    action = ''
    if option =='1':
        print("Calculating Area")  
        speakOut(msg_list[0])
        speakOut("Enter Length")
        l = int(input('Enter Length:'))
        speakOut("Enter Breadth")
        b = int(input('Enter Breadth:'))
        area(l,b)
    elif option == '2':
        print("Calculating Perimeter") 
        speakOut(msg_list[1])
        speakOut("Enter Length")
        l = int(input('Enter Length:'))
        speakOut("Enter Breadth")
        b = int(input('Enter Breadth:'))
        perimeter(l,b)
    elif option =='3':
        speakOut(msg_list[2])
        speakOut("Enter Length")
        l = int(input('Enter Length:'))
        speakOut("Enter Breadth")
        b = int(input('Enter Breadth:'))
        speakOut("Enter Height")
        h = int(input('Enter Height:'))
        volume(l,b,h)
    elif option =='4':
        action = 'Exit'
    else:
        print("Entered the wrong choice")
        speakOut("Entered the wrong choice")
    return action
        
        
"""
main program / master
"""

speech_init()
while True:    
    var = UI()
    todo = decode(var)  
    if todo == 'Exit':
        break
speakOut("Thanks For Using A calculator")
print("Thank you")
speakOut("Thank you")


