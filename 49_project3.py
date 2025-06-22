# hangman project
import random
import hangman_stages
'there will be a choosen word and we cant see it '
'we should guess the letters of that word and we have 6 lives only'
'if we guess all letters crtly the we win'
'if we guess wrong letters and lose 6 lives then we lose'
'i.e if figure of hangman is complete then we lose'
word_list = ['apple', 'beautiful', 'potato', 'mango', 'jayanti',
             'attitude', 'aeroplane']  # creating list of names
chosen_word = random.choice(word_list)  # choosing random name from the list
print("welcome to hangman game\n")
print(hangman_stages.logo)
display = []  # empty list for display
for i in chosen_word:
    display += '_'  # printing blank space according to chosen word
print(display)  # printing blank wordspace
lives = 6  # 6 lives are given
game_over = False  # at first gameover is false
while not game_over:
    # taking input from the user
    guessed_letter = input("guess a letter :").lower()
    for i in range(len(chosen_word)):  # for the xount of chosen word
        letter = chosen_word[i]  # we will put letter of cosen word into letter
        if letter == guessed_letter:  # if guessed letter is same as letter variable
            # we will put guessed letter into that specific position of display
            display[i] = guessed_letter
    print(display)  # we will print updated display
    if guessed_letter not in chosen_word:  # if guessed letter is not in chosen word
        lives -= 1  # life will be lost ,decreased by 1
        if lives == 0:  # if all the lives are gone
            game_over = True  # then game over will be true
            print("you lose")  # then we lose
    if '_' not in display:  # if u gave all ans crt
        game_over = True  # it will end the game
        print("you win!!")  # and u win
    print(hangman_stages.stages[lives])  # it will print accodingly
