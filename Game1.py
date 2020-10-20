#Rohan Rao

import random
import time

name = input("What is your name? ")

print("Good Luck ! ", name)

# Word bank
# Words to guess from
words = ['banana','strawberry','mango','blueberry',
'pineapple','apple','raspberry','blackberry','orange','pear',
'grape','peach','kiwi']

#Chooses randomn word
word = random.choice(words)
print("Guess the characters")
hangman = "  0"
hangman2 = "\n/"
hangman3 = "|"
hangman4 = "\ "

hangman5 = "\n /"

hangman6 = "\ "

print(hangman, hangman2, hangman3, hangman4, hangman5, hangman6)

print("The Theme is Fruits")
guesses = ''
turns = 6
while turns > 0:
    failed = 0

    for char in word:

        if char in guesses:
            print(char, end = " ")
        else:
            print("_", end = " ")
            failed += 1

    if failed == 0:
        print("You Win!")
        print("The word is:", word)
        break

    guess = input("guess a character:")

    guesses += guess
# If the letter guessed is not in the word it removes a turn
    if guess not in word:

        turns -= 1

        print("Wrong")
        print("You have", + turns, 'more guesses')

# When user runs out of turns
if turns == 0:
    print("GAME OVER YOU LOSE! The word was", word)
    print("Would you like to play again? ")
