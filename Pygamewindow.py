# Rohan Rao
# Pygame Window Assignment
# This program asks the user for the width and height of the window as
# well as the color of the window
# With this information, the program makes a window with the size given
# to fill up with that color

import pygame
import time
pygame.init()

size = input("Would you like the width/height to be 1000 x 1000? ")
if size == "no":
    size2 = input("Ok, would 500 x 500 be okay? ")
    if size2 == "yes":
        screen = pygame.display.set_mode((500,500))
    if size2 == "no":
        print("Sorry, we don't have other sizes...")
        time.sleep(3)
        quit()
if size == "yes":
    screen = pygame.display.set_mode((1000,1000))
pygame.display.flip()
pygame.display.set_caption("Pygame Window")
color = input("Enter the color of the window: ")
if color == "red":
    screen.fill((255,0,0))
    pygame.display.update()
if color == "orange":
    screen.fill((255,128,0))
    pygame.display.update()
if color == "yellow":
    screen.fill((255,255,0))
    pygame.display.update()
if color == "green":
    screen.fill((0,204,0))
    pygame.display.update()
if color == "blue":
    screen.fill((0,0,255))
    pygame.display.update()
if color == "purple":
    screen.fill((127,0,125))
    pygame.display.update()
if color == "pink":
    screen.fill((255,0,255))
    pygame.display.update()
if color == "black":
    screen.fill((0,0,0))
    pygame.display.update()
if color == "white":
    screen.fill((255,255,255))
    pygame.display.update()
