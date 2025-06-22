# project 9 coffee machine project
'it will ask for diff types of coffees and calculate price and return change'
'type off to turnoff and type report to check ingrediants left in machine and amount collected'

profit = 0  # here at start profit will be zero
resources = {  # resources at start
    'water': 500,
    'milk': 200,
    'coffee': 100
}

menu = {  # menu which has 3 coffee in that ingrediants and cost, in ingrediants 3 items
    "latte": {
        "ingrediants": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 150
    },
    "espresso": {
        "ingrediants": {
            "water": 50,
            "coffee": 18
        },
        "cost": 100
    },
    "cappuccino": {
        "ingrediants": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 200
    }
}


# function to check if resources have sufficient ingrediants required
def check_resources(order_ingrediants):
    for item in order_ingrediants:
        # if required ingrediants >resource
        if order_ingrediants[item] > resources[item]:
            print(f"sorry there is not enough {item}")
            return False  # not enough
    return True  # true if sufficient ingrediants are present


def process_coins():  # function to calculate the total amount gave by customer
    print("please insert the coins:")
    total = 0
    coins_five = int(input("how many 5rs coins? "))
    coins_ten = int(input("how many 10rs coins? "))
    coins_twenty = int(input("how many 20rs coins? "))
    total = (coins_five*5)+(coins_ten*10)+(coins_twenty*20)
    return total  # return total amount


# function to check if payment is done or no
def is_payment_successful(money_recieved, coffee_cost):
    if money_recieved >= coffee_cost:
        global profit  # to access and modify global variabel in function
        profit += coffee_cost  # if payment is sufficient then add to profit
        change = money_recieved-coffee_cost  # calculate change
        print(f"here is your {change}rs in change")  # and return change
        return True  # if true then next will make a coffee
    else:
        print("sorry thats not enough money, money refunded")
        return False  # it will not make a coffee and print not suficient


# function to deduct ingrediants from resources
def make_coffee(coffee_name, coffee_ingrediants):
    for item in coffee_ingrediants:
        # this loop will minus all required ingrediants from resource ingrediants
        resources[item] -= coffee_ingrediants[item]
        # and will print coffee name and is ready
    print(f"here is you {coffee_name}.!!!!!!!!")


is_on = True  # condition for while loop to run machine again and again
while is_on:
    'it will take input of coffee name or off or report'
    choice = input(
        "what would u like latte/espresso/cappuccino, type 'off' to turnoff machine,'report' to see left ingrediants")
    if choice == 'off':  # if off
        is_on = False  # out of the game
    elif choice == 'report':  # if report print left resource ingrediants and profit earned
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}gm")
        print(f"money:{profit}rs")
    else:
        # store dictionary of particular coffee from menu into coffee_type
        coffee_type = menu[choice]
        'this loop will check if resources are availabel or no'
        # if return value is true then enters this loop
        if check_resources(coffee_type['ingrediants']):
            payment = process_coins()  # if sufficient ingrediants are there,find total payment done
            # if return value is true then enters this loop
            if is_payment_successful(payment, coffee_type['cost']):
                # if payment is successful deduct in resources and make a coffee
                make_coffee(choice, coffee_type['ingrediants'])
