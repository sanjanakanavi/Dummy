# silent auction program (project5)
'collect bidder names and price and then find the max price and declare winner'
import os
print("********Welcome to silect auction program********")
bidder_data = {}  # taking one empty dictionary


def find_winner(bidder_details):
    highest_bid = 0  # to store the highest price
    winner = ""  # to store the name of the winner
    for bidder in bidder_details:  # iterating dictionary
        # extracting corresponding price
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price  # storing highest price in variable
            winner = bidder  # storing name of winner
    print(bidder_details)
    # priting result
    print(f"the winner is {winner} with a bid price of {highest_bid}")


end_of_bidding = False  # taking a flag to control while loop
while not end_of_bidding:
    name = input("what is your name?\n")
    # taking inputs name and bid price
    price = int(input("what is your bid?:\n"))
    bidder_data[name] = price  # adding inputs into dictionary
    # asking again in lower case
    more_bidders = input(
        "are there more bidders? type 'yes' or 'no'\n").lower()
    if more_bidders == 'no':  # if no more bidders
        end_of_bidding = True  # then loop should stop by making it true
        find_winner(bidder_data)  # calling function to return a winner
    elif more_bidders == 'yes':
        # method to clear the previous screen of output of code
        os.system('cls')
