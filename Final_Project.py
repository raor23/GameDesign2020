# Rohan Rao
# Help from Dad
# This is my final project for Game Design
# This game is popular and is known as "Flappy Bird"
# It has 3 difficulties (Easy, Medium, and Hard)
# which changes the scrolling speed to make it harder
# I don't have a leaderboard because
# Flappy Bird doesn't usually have a leaderboard
# This code ALMOST works fully but the game is still playable

# Pseudo code:
# import pygame modules
# initialize pygame
# set dimenisons of pygame window (height, width, caption, etc.)
# define fonts (for menu and instructions)
# load images (background, pipes, etc.)
# define color
# draw buttons for main menu
# define game variables (scrolling speed, score, menu and game loops, etc.)
# define game functions (frequency for pipes, score, etc.)
# run menu loop (background, and buttons)
# if click difficulty, run main game loop
# after game, 3 buttons are drawn (restart with same difficulty, quit, or back to menu)
# screen is 846 by 936 pixels



# import modules
import pygame
from pygame.locals import *
import random

#initialize pygame
pygame.init()

clock = pygame.time.Clock()
fps = 60

#set screen dimensions
screen_width = 864
screen_height = 936

#set caption of pygame window
pygame.display.set_caption('Flappy Bird')

#define font
font = pygame.font.SysFont('Bauhaus 93', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
TITLE_FONT2 = pygame.font.SysFont('comicsans', 70)
BUTTON1FONT = pygame.font.SysFont('comicsans', 60)
BUTTON2FONT = pygame.font.SysFont('comicsans', 60)
BUTTON3FONT = pygame.font.SysFont('comicsans', 60)
BUTTON4FONT = pygame.font.SysFont('comicsans', 60)
INSTRUCTIONSFONT = pygame.font.SysFont('comicsans', 60)

#define colors
white = (25, 255, 255)

#define game variables
screen = pygame.display.set_mode((screen_width, screen_height))
ground_scroll = 0
scroll_speed = 0
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False
menu = True
run = False


#drawing main menu buttons
# setting dimensions ( x   y   w   h)
button1 = pygame.Rect(232,200,400,50)
button2 = pygame.Rect(307,275,250,50)
button3 = pygame.Rect(307,350,250,50)
button4 = pygame.Rect(307,425,250,50)

#drawing text on main menu buttons
text1 = BUTTON1FONT.render("INSTRUCTIONS [1]", 1, (0,0,0))
text2 = BUTTON2FONT.render("EASY [2]", 1, (0,0,0))
text3 = BUTTON3FONT.render("MEDIUM [3]", 1, (0,0,0))
text4 = BUTTON4FONT.render("HARD [4]", 1, (0,0,0))

#drawing text for instructions        Text            color
text5 = INSTRUCTIONSFONT.render("INSTRUCTIONS:", 1, (0,0,0))
text6 = INSTRUCTIONSFONT.render("THE OBJECTIVE OF FLAPPY BIRD", 1, (0,0,0))
text7 = INSTRUCTIONSFONT.render("IS TO KEEP YOUR BIRD IN BETWEEN", 1, (0,0,0))
text8 = INSTRUCTIONSFONT.render("THE PIPES IN ORDER FOR IT TO FLY", 1, (0,0,0))
text9 = INSTRUCTIONSFONT.render("THROUGH. EVERY TIME YOU GET THE", 1, (0,0,0))
text10 = INSTRUCTIONSFONT.render("BIRD IN BETWEEN THE PIPES, YOU GET", 1, (0,0,0))
text11 = INSTRUCTIONSFONT.render("A POINT. TO MAKE THE BIRD FLY, CLICK", 1, (0,0,0))
text12 = INSTRUCTIONSFONT.render("THE MOUSEPAD. THIS IS AN ENDLESS", 1, (0,0,0))
text13 = INSTRUCTIONSFONT.render("GAMEMODE (IT KEEPS GOING UNTIL YOU", 1, (0,0,0))
text14 = INSTRUCTIONSFONT.render("DIE). THE DIFFICULTY IS BASED ON ", 1, (0,0,0))
text15 = INSTRUCTIONSFONT.render("HOW FAST THE BIRD MOVES.", 1, (0,0,0))
text16 = INSTRUCTIONSFONT.render("Click 1 to go to menu", 1, (0,0,0))


#loading images for game
bg = pygame.image.load('bg.png')
ground_img = pygame.image.load('ground.png')
button_img = pygame.image.load('restart.png')
button_2_img = pygame.image.load('exit.png')
button_3_img = pygame.image.load('menu.png')
MenuTitle =  pygame.image.load('FlappyBirdMenuTitle.png')

#DEFINING FUNCTIONS

#Function for instructions
def instructions():
        screen.fill(white)
        #screen_width/2 - text{num}.get_width()/2 is for centering
        #            Text                  x                       y
        screen.blit(text5, (screen_width/2 - text5.get_width()/2, 50))
        screen.blit(text6, (screen_width/2 - text6.get_width()/2, 100))
        screen.blit(text7, (screen_width/2 - text7.get_width()/2, 150))
        screen.blit(text8, (screen_width/2 - text8.get_width()/2, 200))
        screen.blit(text9, (screen_width/2 - text9.get_width()/2, 250))
        screen.blit(text10, (screen_width/2 - text10.get_width()/2, 300))
        screen.blit(text11, (screen_width/2 - text11.get_width()/2, 350))
        screen.blit(text12, (screen_width/2 - text12.get_width()/2, 400))
        screen.blit(text13, (screen_width/2 - text13.get_width()/2, 450))
        screen.blit(text14, (screen_width/2 - text14.get_width()/2, 500))
        screen.blit(text15, (screen_width/2 - text15.get_width()/2, 550))
        screen.blit(text16, (screen_width/2 - text16.get_width()/2, 750))

        keys = pygame.key.get_pressed()
        # If key 1 is pressed, user returns to menu
        # (Not working)
        if keys[pygame.K_1]:
                menu = True

        pygame.display.update()

#Function for drawing text on the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

#Function for resetting game after loss
def reset_game():
	pipe_group.empty()
	flappy.rect.x = 100
	flappy.rect.y = int(screen_height / 2)
	score = 0
	return score


class Bird(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range (1, 4):
			img = pygame.image.load(f"bird{num}.png")
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
		self.clicked = False

	def update(self):

		if flying == True:
			#apply gravity
			self.vel += 0.5
			if self.vel > 8:
				self.vel = 8
			if self.rect.bottom < 768:
				self.rect.y += int(self.vel)

		if game_over == False:
			#jump
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				self.vel = -10
			if pygame.mouse.get_pressed()[0] == 0:
				self.clicked = False

			#handle the animation
			flap_cooldown = 5
			self.counter += 1

			if self.counter > flap_cooldown:
				self.counter = 0
				self.index += 1
				if self.index >= len(self.images):
					self.index = 0
				self.image = self.images[self.index]


			#rotate the bird
			self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
		else:
			#point the bird at the ground
			self.image = pygame.transform.rotate(self.images[self.index], -90)


#Class for drawing pipes' sprites
class Pipe(pygame.sprite.Sprite):

	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("pipe.png")
		self.rect = self.image.get_rect()
		#position variable determines if the pipe is coming from the bottom or top
		#position 1 is from the top, -1 is from the bottom
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
		elif position == -1:
			self.rect.topleft = [x, y + int(pipe_gap / 2)]


	def update(self):
		self.rect.x -= scroll_speed
		if self.rect.right < 0:
			self.kill()


#Class for buttons at end of game
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def draw(self):
		action = False

		#get mouse position
		pygame.init()
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				action = True

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action



pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)

#drawing restart button (after loss)
button = Button(screen_width // 2 - 50, screen_height // 2 - 250, button_img)
#drawing exit button (after loss)
button_2 = Button(screen_width // 2 - 50, screen_height // 2 - 150, button_2_img)
#drawing menu button (after loss)
button_3 = Button(screen_width // 2 - 50, screen_height // 2 - 200, button_3_img)


# MAIN PROGRAM (while loops)

# Menu loop
while menu:
        #draw background
        screen.blit(bg, (0,0))
        #draw menu title on background
        screen.blit(MenuTitle, (175,-100))

        #draw main menu buttons
        pygame.draw.rect(screen,(0,102,0), button1)
        pygame.draw.rect(screen,(0,102,0), button2)
        pygame.draw.rect(screen,(0,102,0), button3)
        pygame.draw.rect(screen,(0,102,0), button4)

        screen.blit(text1, (screen_width/2 - text1.get_width()/2, 210))
        screen.blit(text2, (screen_width/2 - text2.get_width()/2, 285))
        screen.blit(text3, (screen_width/2 - text3.get_width()/2, 360))
        screen.blit(text4, (screen_width/2 - text4.get_width()/2, 435))


        #checking for if a key pressed
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1: # button to instructions
                                menu = False
                                instructions()
                        if event.key == pygame.K_2: # button to easy difficulty
                                scroll_speed = 4 # Changing scroll speed as difficulty goes up
                                menu = False
                                run = True
                        if event.key == pygame.K_3: # button to medium difficulty
                                scroll_speed = 10
                                menu = False
                                run = True
                        if event.key == pygame.K_4: # button to hard difficulty
                                scroll_speed = 20
                                menu = False
                                run = True

        # updating display to actually display it on the pygame window
        pygame.display.update()

# Main Game Loop
while run:
        #draw background
        screen.blit(bg, (0,0))

        clock.tick(fps)
        #draw pipes and bird
        pipe_group.draw(screen)
        bird_group.draw(screen)
        bird_group.update()

	#draw and scroll the ground
        screen.blit(ground_img, (ground_scroll, 768))

	#check the score
    #check if the bird actually passes through the pipe
        if len(pipe_group) > 0:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
                   and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
			and pass_pipe == False:
                        pass_pipe = True
                if pass_pipe == True:
                        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                                score += 1
                                pass_pipe = False
        draw_text(str(score), font, white, int(screen_width / 2), 20)


	#look for collision to pipe
    #if bird collides, it is game over
        if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
                game_over = True
	#once the bird has hit the ground it's game over and no longer flying
        if flappy.rect.bottom >= 768:
                game_over = True
                flying = False

        #if the bird is flying and it is not game over
        if flying == True and game_over == False:
                #it will generate new pipes for the player to pass through
                time_now = pygame.time.get_ticks()
                if time_now - last_pipe > pipe_frequency:
                        pipe_height = random.randint(-100, 100)
                        btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
                        top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
                        pipe_group.add(btm_pipe)
                        pipe_group.add(top_pipe)
                        last_pipe = time_now

                pipe_group.update()

                ground_scroll -= scroll_speed
                if abs(ground_scroll) > 35:
                        ground_scroll = 0

        #Buttons at the end of the game
        if game_over == True:
                if button.draw(): # Restart Button
                        game_over = False
                        score = reset_game()
                        pygame.display.update()
                if button_2.draw(): # Exit Button
                        pygame.display.quit()
                if button_3.draw(): # Return to menu Button (not working)
                        menu = True

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
                        flying = True

        pygame.display.update()

pygame.quit()
