# -*- coding: utf-8 -*-
from Phygital_v0 import Phygital_v0 as phy
import time 

phy.init("COM10") #Add the COM Port Number Here

while True:      
    phy.MoveServo(9,90)
            
    time.sleep(1)
            
    phy.MoveServo(9,90)
            
    time.sleep(1)
        
    
print("Closing")
