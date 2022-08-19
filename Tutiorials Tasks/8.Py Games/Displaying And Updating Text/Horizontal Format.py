import pygame
import time

pygame.init()

Width = 558
Height = 418

screen = pygame.display.set_mode((Width,Height))

screen = pygame.display.set_mode((Width,Height))

ScreenImage = pygame.image.load("Iamges/Background Image.png")

screen.blit(ScreenImage,(0,0))

EventStatus="None"

num = 0


while True:
    pygame.display.update()
    for i in range (1):
        font = pygame.font.SysFont("Eras Bold ITC",50)
        text= font.render(str(num),True,(255,0,0))
        screen.blit(text,(100,100)      
        
    
    
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            EventStatus="Quit"
            break
       
        
    if EventStatus == "Quit":
        break
    
print("Closing")