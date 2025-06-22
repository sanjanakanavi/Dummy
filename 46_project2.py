# password generator project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to password generator")
n_letters = int(input("how many letters you want in ur password?\n"))
n_numbers = int(input("how many numbers you want in ur password?\n"))
n_symbols = int(input("how many symbols you want in ur password?\n"))
password_list = []  # mpty list to store the data
for i in range(1, n_letters+1):
    # using random.choice to select random element from lists
    char = random.choice(letters)
    password_list += char
for i in range(1, n_numbers+1):
    char = random.choice(numbers)
    password_list += char
for i in range(1, n_symbols+1):
    char = random.choice(symbols)
    password_list += char
random.shuffle(password_list)  # shuffling the result list
password = ""  # empty string to create password
for i in password_list:
    password += i  # converting list to string
print("you password is:", password)
