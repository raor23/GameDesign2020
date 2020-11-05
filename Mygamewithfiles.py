# Rohan Rao
# Unscramble Word 1-Player game
# Using files for scoreboard

# import random module
import random
import csv

menu = int(input("""****************************************
*                                      *
*    Welcome to Unscramble the word!   *
*           Press 1 to play            *
*       Press 2 for Instructions       *
*        Press 3 for Scoreboard        *
*           Press 4 to quit            *
*                                      *
****************************************\n"""))



# function for choosing random word.
def choose():
	# list of word
	Fruits = ['apple','banana','pear','peach',
              'strawberry','blueberry','cherry',
			  'grape','avocado','watermelon',
			  'orange','plum','mango','papaya',
			  'raspberry','blackberry','tomato']

	# choice() method randomly chooses
	# any word from the list.
	pick = random.choice(Fruits)

	return pick


# Function for shuffling the
# characters of the chosen word.
def jumble(word):
	# sample() method shuffling the characters of the word
	random_word = random.sample(word, len(word))

	# join() method join the elements
	# of the iterator(e.g. list) with particular character .
	jumbled = ''.join(random_word)
	return jumbled


# Function for showing final score.
def thank(p1n, p1):
	print(p1n,'Your score is :', p1)


	ask = input("Would you like to play again? ")
	if ask == "yes":
		while True:
			play()
	elif ask == "no":
		ansmenu = input("Would you like to go back to the menu? ")
		if ansmenu == "yes":
			menu = int(input("""****************************************
*                                      *
*    Welcome to Unscramble the word!   *
*           Press 1 to play            *
*       Press 2 for Instructions       *
*        Press 3 for Scoreboard        *
*           Press 4 to quit            *
*                                      *
****************************************\n"""))
		elif ansmenu == "no":
			print("Thanks for Playing!")
			quit()


# Function for playing the game.
def play():
	# enter player1 and player2 name
	p1name = input("Please enter your name: ")
	print("The Theme is Fruits")

	pp1 = 0

	# variable for counting turn
	turn = 2

	# keep looping
	while True:

		# choose() function calling
		picked_word = choose()

		# jumble() fucntion calling
		qn = jumble(picked_word)
		print("The Scrambled word is :", qn)

		# checking turn is odd or even
		if turn % 2 == 0:


			ans = input("What's the word? ")

			# checking ans is equal to picked_word or not
			if ans == picked_word:

				pp1 += 1

				print('Your score is :', pp1)

			else:
				print("Better luck next time...correct word is : ", picked_word)
				while True:
					print("You have no more guesses...You Loose!")
					user = str(input("Enter a name to save your highscore: "))
					with open('scoreboard.csv', 'a') as f:
						writer = csv.writer(f)
						writer.writerow([user, f"{pp1}pts"])
					break

				c = int(input("press 1 to continue and 0 to quit : "))

				# checking the c is equal to 0 or not
				# if c is equal to 0 then break out
				# of the while loop o/w keep looping.
				if c == 0:
					# thank() function calling
					thank(p1name, pp1)
					break

if menu == 1:
	while True:
		play()
if menu == 2:
        print("""Instructions: You have to unscramble the word and type
	      in the word that you think it is. If you get it right,
	      you get a point. If you get it wrong, the other player
	      gets to take a guess. And if both of the players guess wrong,
	      the game tells you the word and moves on to the next word.
	      You can choose to quit or continue after every round (each player goes).""")
if menu == 3:
        myFile = open("scoreboard.csv", "r")
        print(myFile.read())
	

if menu == 4:
        quit()

# Driver code
if __name__ == '__main__':

	# play() function calling
	play()
