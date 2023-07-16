import random
import os




print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")


GUESSES_LEFT = 0
def difficulty_select():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
    if difficulty == "easy":
        GUESSES_LEFT = 10
    elif difficulty == "hard":
        GUESSES_LEFT= 5
    else: 
        difficulty_select()
    return GUESSES_LEFT

GUESSES_LEFT = difficulty_select()

print(f"You have {GUESSES_LEFT} attempts remaining to guess the number.")

COMPUTER_NUMBER = random.randint(1,100)


def guessing_game(guesses_left, COMPUTER_NUMBER):

    user_number = int(input("Make a guess:"))
    computer_number = COMPUTER_NUMBER
    if guesses_left == 0:
        print(f"Game Over, You Lost, the number was {computer_number}")
        os.close
    else:
        guesses_left -= 1
        if user_number > COMPUTER_NUMBER:
            print("Too high")
            guessing_game(guesses_left,COMPUTER_NUMBER)
        elif user_number < COMPUTER_NUMBER:
            print("Too low")
            guessing_game(guesses_left,COMPUTER_NUMBER)
        else:
            print(f"You guessed it!, the number was {computer_number}")


guessing_game(GUESSES_LEFT,COMPUTER_NUMBER)

