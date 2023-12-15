'''balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    # to make the global variable being introduced to the local function
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()
    '''
## Trying the same excercise of bank deposit and withdraw but using Class instead of functions

class Account:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, n):
        self.balance += n

    def withdraw(self, n):
        self.balance -= n

def main():
        account = Account()
        print("Balance:", account.balance)
        account.deposit(150)
        account.withdraw(50)
        print("Balance:", account.balance)

if __name__ == "__main__":
    main()