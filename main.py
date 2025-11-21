"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars
balance = 1000000
i = balance

print(f"Your current balance is {balance}")

def deposit() :
    amount = int(input("how much would you like to deposit"))
    global balance
    balance += amount
    if balance >=0 :
        balance == True
        print(f"You have deposited {amount}.")
        bal_draw = input("Would you like to withdraw money (w), deposit money (d), or check your balance (b)?")
        if bal_draw == "w" :
            withdraw()
        elif bal_draw == "d" :
            deposit()
        elif bal_draw == "b" :
            check_balance()
        else:
            print("that is not an option")
            print("that is not an option")
    elif balance <= 0:
        balance == False
        shutdown()
    else:
        print("The ATM is broken")

def withdraw() :
    amount = int(input("how much would you like to withdraw"))
    global balance
    balance -= amount
    if balance >=0 :
        balance == True
        print(f"You have withdrawn {amount}.")
        bal_draw = input("Would you like to withdraw money (w), deposit money (d), or check your balance (b)?")
        if bal_draw == "w" :
            withdraw()
        elif bal_draw == "d" :
            deposit()
        elif bal_draw == "b" :
            check_balance()
        else:
            print("that is not an option")
    elif balance <= 0:
        balance == False
        shutdown()
    else:
        print("The ATM is broken")



def check_balance():
    print(f"Your current balance is {balance}")
    bal_draw = input("Would you like to withdraw money (w), deposit money (d), or check your balance (b)?")
    if bal_draw == "w" :
        withdraw()
    elif bal_draw == "d" :
        deposit()
    elif bal_draw == "b" :
        check_balance()
    else:
        print("that is not an option")

"""
try:
    user_input = int(input("Enter an integer: "))
    print("User input is an integer")
except ValueError:
    print("User input is not an integer")
"""
def shutdown():
    for i in range (1):
        print("The ATM is closed.")
        break

while balance >= 0 :
    bal_draw = input("Would you like to withdraw money (w), deposit money (d), or check your balance (b)?")
    if bal_draw == "w" :
        withdraw()
    elif bal_draw == "d" :
        deposit()
    elif bal_draw == "b" :
        check_balance()
    else:
        shutdown()