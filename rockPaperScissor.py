import random

item_list = ['rock', 'paper', 'scissor']

user_choice = input("Pick your choice,rock,paper,scissor: ")
computer_choice = random.choice(item_list)

if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")

if user_choice == 'rock':
    if computer_choice == 'scissor':
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")

if user_choice == 'paper':
    if computer_choice == 'rock':
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")

if user_choice == 'scissor':
    if computer_choice == 'paper':
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
