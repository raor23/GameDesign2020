# Rohan Rao

import pygame
## Drawing with pygame
## ask the user to give you a color
## create the window with that color
## What is the w and h of the window


pygame.init()  # first command
screen = pygame.display.set_mode((800,600)) # this is a tuple
screen.fill((0,0,0)) # You select the color of your background 0-255
pygame.display.flip()
pygame.display.set_caption("Testing pygame") # title for testing pygame
run =True
while run:
    pygame.time.delay(100)
    screen.fill((162,32,69))
    pygame.display.update()
    for eve in pygame.event.get():
        print(eve)
        if eve.type == pygame.QUIT:
            run = False
pygame.time.delay(50)
pygame.quit()
