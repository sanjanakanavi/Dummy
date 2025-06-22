# project8 higher lower game
import project8_database
import random
import os
'comparing 2 datas havinf higher or lower values '
'if wrong answer game ends else adds 1 score to every right answer and return answer'

score = 0  # to store a score


def display_accountinfo(account):  # function to extract data from dictionaries
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # returning a string with data
    return f"{name} ,a {description} , from {country}"


# function to check whose followers are higher and will return true or false
def check_answer(guess, followers_1, followers_2):
    if followers_1 < followers_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False


print(project8_database.game_logo)  # printing the logo
# just to give data to accoun_1 for the first iteration
account_2 = random.choice(project8_database.data)

continue_flag = True  # condition for while loop
while continue_flag:
    # for first iteration it takes from above statement ,after entering loop second account becomes first
    account_1 = account_2
    # it generates random every time
    account_2 = random.choice(project8_database.data)
    while account_1 == account_2:
        # if both are equal then it will generate new until its different
        account_2 = random.choice(project8_database.data)
    # getting data for first
    print(f"compare 1: {display_accountinfo(account_1)}")
    print(project8_database.vs)
    # getting data for second
    print(f"compare 2: {display_accountinfo(account_2)}")
    # storing input in guess variable
    guess = int(input("who has more followers? type 1 or 2\n"))
    # fetching values of both followers account
    followers_count_1 = account_1["follower count"]
    followers_count_2 = account_2["follower count"]
    # and checking if answer is correct or not & will store return value in is_correct variable
    is_correct = check_answer(guess, followers_count_1, followers_count_2)
    os.system('cls')  # clearing the prevoius screen
    print(project8_database.game_logo)  # printing logo every time
    if is_correct == True:  # if answer is correct
        score += 1  # scores up
        # and display and again ask the question,loop continues
        print(f"you are right , your score is {score}")
    else:
        # if answer is wrong ,
        print(f"you are wrong ,your final score is {score}")
        continue_flag = False  # then will come out of the loop
