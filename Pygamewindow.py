# Rohan Rao
# Pygame Window Assignment
# This program asks the user for the width and height of the window as
# well as the color of the window
# With this information, the program makes a window with the size given
# to fill up with that color

import pygame
import time
pygame.init()

height = input("What would you like the height of the window to be? (10-1000): ")
width = input("What would you like the width of the window to be? (10-1000): ")

height = int(height)
width = int(width)

screen = pygame.display.set_mode((height,width))

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
