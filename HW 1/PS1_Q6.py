'''The program allows user to guess a random generated number up to 10 times'''

import random

while True:

    num = random.randint(1, 100)

    print("The random number has been generated")

    print("--------------------------------------------------------------")

    guessed = False

    # User guesses are compared against the random number
    for i in range(0, 10):
        guess = int(input("Try to guess the number: "))
        if guess == num:
            guessed = True
            print("Correct!")
            break
        elif guess > num:
            print("Wrong! The guess is too high \n")
        else:
            print("Wrong! The guess is too low \n")

    print("--------------------------------------------------------------")

    if guessed:
        print("Congratulations, you guessed the number", num)

    else:
        print("Sorry, you did not guess the number", num)

    if (input("Would you like to play again? (Y/N): ")) == "N":
        break
    
    print("--------------------------------------------------------------")
