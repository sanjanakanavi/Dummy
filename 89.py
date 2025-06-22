# coding exercise
'bank account having custemer name and balance,he can withdraw or deposit'


class BankAccount:  # class as bank account
    def __init__(self, name, balance):  # attributes for balance and name
        self.acount_holder = name
        self.balance = balance

    def deposit(self, amount):  # method to deposit money
        self.balance += amount
        print(
            f"Deposited {amount} to your account, your Balance :{self.balance}")

    def withdraw(self, amount):  # method to withdraw money
        if amount > self.balance:  # only if withdrawing money is less then balance
            print("not enough money")
        else:
            self.balance -= amount
            print(f"successfully withdrew ,account balance: {self.balance}")

    def __str__(self):  # string version of object,called automatically when object is created
        return f"AccountHolder name: {self.acount_holder}\nBalance: {self.balance}"


obj = BankAccount("sanjana", 2000)
print(obj)
obj.deposit(1000)
obj.withdraw(500)
