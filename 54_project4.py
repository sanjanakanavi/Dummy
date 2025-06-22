# coding exercise project4
'caesar cipher'
'its a method to encrypt and decrypt the text messages'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # taking a list of alphabets


def encryption(plain_text, shift_key):  # for encryption operation
    cipher_text = ""  # result text of encryption to store
    for char in plain_text:  # iterating characters of input text
        if char in alphabet:  # if char is in list then only it proceeds
            position = alphabet.index(char)  # find the index of that character
            # find new position ,%26 will help if new position exceeds 26 then alphabet loop will start from first index
            new_position = (position+shift_key) % 26
            # will add new position letter of list to result text
            cipher_text += alphabet[new_position]
        else:
            # if char is " "/number/special character then it adds as it is to result text
            cipher_text += char
    print(f"here is the text after encryption: {cipher_text}")


def decryption(cipher_text, shift_key):  # for decryption operation
    plain_text = ""  # result text of decryption to store
    for char in cipher_text:  # iterating characters of input text
        if char in alphabet:  # if char is in list then only it proceeds
            position = alphabet.index(char)  # find the index of that character
            # find new position ,%26 will help if new position exceeds 26 then alphabet loop will start from first index
            new_position = (position-shift_key) % 26
            # will add new position letter of list to result text
            plain_text += alphabet[new_position]
        else:
            # if char is " "/number/special character then it adds as it is to result text
            plain_text += char
    print(f"here is the text after decryption: {plain_text}")


wanna_end = False  # flag to decide if loop should stop or no
while not wanna_end:
    what_to_do = input(
        "type 'encrypt' for encryption and 'decrypt' for decryption:\n")
    text = input("type your messege\n").lower()
    shift = int(input("enter shift key:\n"))
    if what_to_do == "encrypt":
        # using keyword argument method
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    # taking input from user
    play_again = input("type 'yes' to continue, type 'no' to exit:\n")
    if play_again == 'no':  # if user wants to stop the game
        wanna_end = True  # turn flag variable into true
        print("have a nice day, bye!!!")
