# Rohan Rao
# Unscramble Word 2-Player game

# import random module
import random


menu = int(input("""****************************************
*                                      *
*    Welcome to Unscramble the word!   *
*           Press 1 to play            *
*       Press 2 for Instructions       *
*            Press 3 to quit           *
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
def thank(p1n, p2n, p1, p2):
	print(p1n, 'Your score is :', p1)
	print(p2n, 'Your score is :', p2)

	# check_win() function calling
	check_win(p1n, p2n, p1, p2)

	ask = input("Would you like to play again?")
	if ask == "yes":
		while True:
			play()
	elif ask == "no":
		print("Thanks for Playing!")
		quit()


# Function for declaring the winner
def check_win(player1, player2, p1score, p2score):
	if p1score > p2score:
		print("The winner is ", player1)
	elif p2score > p1score:
		print("The winner is ", player2)
	else:
		print("Its a tie!")


# Function for playing the game.
def play():
	# enter player1 and player2 name
	p1name = input("player 1, Please enter your name :")
	p2name = input("Player 2 , Please enter your name: ")
	print("The Theme is Fruits")

	# variable for counting score.
	pp1 = 0
	pp2 = 0

	# variable for counting turn
	turn = 0

	# keep looping
	while True:

		# choose() function calling
		picked_word = choose()

		# jumble() fucntion calling
		qn = jumble(picked_word)
		print("The Scrambled word is :", qn)

		# checking turn is odd or even
		if turn % 2 == 0:

			# if turn no. is even
			# player1 turn
			print(p1name,', it is your Turn.')

			ans = input("What's the word? ")

			# checking ans is equal to picked_word or not
			if ans == picked_word:

				pp1 += 1

				print('Your score is :', pp1)
				turn += 1

			else:
				print("Better luck next time ..")

				# player 2 turn
				print(p2name, ', it is your turn.')

				ans = input('Guess the word!')

				if ans == picked_word:
					pp2 += 1
					print("Your Score is :", pp2)

				else:
					print("Better luck next time...correct word is :", picked_word)

				c = int(input("press 1 to continue and 0 to quit :"))

				# checking the c is equal to 0 or not
				# if c is equal to 0 then break out
				# of the while loop o/w keep looping.
				if c == 0:
					# thank() function calling
					thank(p1name, p2name, pp1, pp2)
					break

		else:

			# if turn no. is odd
			# player2 turn
			print(p2name, ', it is your turn.')
			ans = input('Guess the word! ')

			if ans == picked_word:
				pp2 += 1
				print("Your Score is :", pp2)
				turn += 1

			else:
				print("Better luck next time.. :")
				print(p1name, ', it is your turn.')
				ans = input('Guess the word! ')

				if ans == picked_word:
					pp1 += 1
					print("Your Score is :", pp1)

				else:
					print("Better luck next time...correct word is :", picked_word)

					c = int(input("press 1 to continue and 0 to quit :"))

					if c == 0:
						# thank() function calling
						thank(p1name, p2name, pp1, pp2)
						quit()
						break

			c = int(input("press 1 to continue and 0 to quit :"))
			if c == 0:
				# thank() function calling
				thank(p1name, p2name, pp1, pp2)
				break
if menu == 1:
	while True:
		play()
if menu == 2:
        print("""Instructions: You have to unscramble the word and type
	      in the word that you think it is. If you get it right,
	      you get a point. If you get it wrong, the otehr player
	      gets to take a guess. And if both of you get it wrong,
	      it tells you the word and moves on to the next word.
	      You can choose to quit or continue after every round.""")
if menu == 3:
        quit()

# Driver code
if __name__ == '__main__':

	# play() function calling
	play()
