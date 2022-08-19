import time

done = 0

print(" ")
print("IN THIS PROGRAM WE WOULD KNOW WHAT IS THE TYPE AND COLOUR OF FLAME , WHAT TYPE OF RESIDUE IS THERE AND WHAT IS THE SMELL WHEN THE FABRIC IS BURNED.")
print(" ")
print("IN THIS PROGRAM THERE WOULD BE 4 FABIERS AS THE FOLLOWING")
print(" ")
print("1.COTTON")
print(" ")
print("2.NYLON")
print(" ")
print("3.POLYESTER")
print(" ")
print("4.SILK")
print(" ")
print("5.RAYON")
print(" ")
print("6.LINEN")
print(" ")
print("7.TENCEL")
print(" ")
print("8.WOOL")
print(" ")
print("9.ACRYLIC")
print(" ")
print("10.ACETATE")

Greetings = input("ENTER YOUR NAME:")

print(" ")
print("Hi!",(Greetings),"!!Your Most Welcome")

while done == 0:
    FIBER = int(input("ENTER THE NUMBER OF THE FBRIC YOU WANT TO KNOW:"))

    if FIBER == 1:
        print(" ")
        print("IT'S COTTON")
        time.sleep(2)
        print(" ")
        print("TYPE AND COLOUR OF FLAME: Yellow,Burns rapidly, clear flame, afterglow")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Yellow,Burns rapidly, clear flame, afterglow")
        time.sleep(2)
        print(" ")
        print("SMELL:Burning paper")
        
    elif FIBER == 2:    
        print(" ")
        print("IT'S NYLON")
        time.sleep(2)
        print(" ")
        print("TYPE AND COLOUR OF FLAME:Does not flame, seems to melt")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Hard bead, cannot be crushed")
        time.sleep(2)
        print(" ")
        print("SMELL:Chemical")
        
    elif FIBER == 3:
        print(" ")
        print("IT'S POLYESTER")
        time.sleep(2)
        print(" ")
        print("TYPE AND COLOUR OF FLAME:Burns slowly, shrinks from flame giving off black smoke")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Hard, cream-colored bead that becomes darker tan")
        time.sleep(2)
        print(" ")
        print("SMELL:Chemical")

    elif FIBER == 4:
        print(" ")
        print("IT'S SILK")
        time.sleep(2)
        print(" ")
        print("TYPE AND COLOUR OF FLAME:Burns slowly, shrinks from flame but does not melt")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Small, brittle beads")
        time.sleep(2)
        print(" ")
        print("SMELL:Burning hair or feathers")

    elif FIBER == 5:
        print(" ")
        print("IT'S RAYON")
        time.sleep(2)
        print(" ")
        print("TYPE OF COLOUR AMD FLAME: Burns less rapidly than cotton with slight melting, no afterglow")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Soft black ash")
        time.sleep(2)
        print("SMELL:Burning paper")
        
    elif FIBER == 6:
        print(" ")
        print("IT'S LINEN")
        time.sleep(2)
        print(" ")
        print("TYPE AND COLOUR OF FLAME:Burns less rapidly than cotton")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Light body ash in shape of cloth")
        time.sleep(2)
        print(" ")
        print("SMELL:Burning paper")
        
    elif FIBER == 7:
        print(" ")
        print("IT'S TENCEL")
        time.sleep(2)
        print(" ")
        print("TYPE AND COLOUR OF FLAME:Continues burning after flame is removed, yellow flame")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Grey ash")
        time.sleep(2)
        print(" ")
        print("SMELL:Burning wood")
        
    elif FIBER == 8:
        print(" ")
        print("IT'S WOOL")
        time.sleep(2)
        print(" ")
        print("TYPE AND COLOUR OF FLAME:Burns slowly, orange flame, shrinks from flame but does not melt")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Large bead or ball, brittle, easily crushed")
        time.sleep(2)
        print(" ")
        print("SMELL:Burning hair or feathers")

    elif FIBER == 9:
        print(" ")
        print("IT'S ACRYLIC")
        time.sleep(2)
        print(" ")
        print("TYPE AND COLOUR OF FLAME:Flames and burns rapidly with hot, sputtering flame, black smoke")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Irregularly-shaped black bead")
        time.sleep(2)
        print(" ")
        print("SMELL:Fishy odor")
        
    elif FIBER == 10:
        print(" ")
        print("IT'S ACETATE")
        time.sleep(2)
        print(" ")
        print("TYPE AND COLOUR OF FLAME:Flames and burns rapidly, double check by placing in nail polish remover- it will dissolve")
        time.sleep(2)
        print(" ")
        print("RESIDUE:Hard, dark, solid bead")
        time.sleep(2)
        print(" ")
        print("SMELL:Burning paper and hot vinegar")

        
    More = input("DO YOU WANT TO TRY FOR MORE  ?:")
    
    if More =="Yes" or More =="yes":
        done = 0
    else:
        done = 1
        print("HAVE A NICE DAY")
