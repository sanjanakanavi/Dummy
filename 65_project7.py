# guess the number project 7
import random
'guess a number from 1 to 50'
'u will have 10 chance for easy level and 5 for hard level'
'u have to guess the crt number'
EASY_ATTEMPTS = 10  # sets no of attempts as global variables
HARD_ATTEMPTS = 5


def set_difficulty(level_chosen):  # function to get attempt numbers
    if level_chosen == 'easy':
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def check_answer(guessed_number, answer, attempts):  # function to check the answer
    if guessed_number < answer:
        print("your guess is too low")
        return attempts-1  # decreasing attempts for wrong answer
    elif guessed_number > answer:
        print("your guess is too high")
        return attempts-1
    else:
        print(f"your guess is right  ,the answer was {answer}")


def game():
    print("$$$$$$$$$$$ guess the number $$$$$$$$$$")
    print("let me think of a number between 1 to 50!!!!")
    answer = random.randint(1, 50)  # generating random number
    # choosing easy or hard
    level = input("choose level of difficulty ....type 'easy' or 'hard' ")
    # according to easy or hard attempts get fixed here
    attempts = set_difficulty(level)
    guessed_number = 0  # empty varible to store guessed number
    while guessed_number != answer:  # if guessed number is not equal
        # printing left attempts
        print(f"you have {attempts} remaining attempts to guess the number.")
        # taking input of guessed number again
        guessed_number = int(input("guess a number"))
        # calling function to check the answer
        attempts = check_answer(guessed_number, answer, attempts)
        if attempts == 0:  # if attempts become 0
            print("you are out of guesses ... you lose:(")
            return  # by return u will come of this whole function
        elif guessed_number != answer:  # this condition helps to not print"guess again" if guessed number=answer
            print("guess again")


game()  # calling a function
