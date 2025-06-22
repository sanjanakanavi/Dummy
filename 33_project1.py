# rock paper scissor game
import random
'there are 9 probabilities of choices from 2 players'
'rock wins against scissors'
'scissors wins against paper'
'paper wins against rock'
"""0-->rock
   1-->paper
   2-->scissors  
users choice     computers choice
0                  0 -->draw           #
0                  1 -->computer wins  @
0                  2 -->user wins      %
1                  0 -->user wins      $
1                  1 -->draw           #
1                  2 -->computer wins  @
2                  0 -->computer wins  %
2                  1 -->user wins      $
2                  2 -->draw           #
for @ cases computer choice > user choice
for # cases computer choice = user choice
for $ cases user choice > computer choice
for % cases user choice < 2(computer choice)
            computer choice < 2(user choice)"""
user_choice = int(
    input("enter ur choice: 0 for rock, 1 for paper, 2 for scissors."))
if user_choice >= 3 or user_choice < 0:
    print("invalid number ,please enter again")
else:
    computer_choice = random.randint(0, 2)
    print(f"your choice : {user_choice} ,computer choice : {computer_choice}")
    if computer_choice == user_choice:
        print("its a draw")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose")
    elif computer_choice == 2 and user_choice == 0:
        print("you win")
    elif computer_choice > user_choice:
        print("you lose")
    elif computer_choice < user_choice:
        print("you win")
