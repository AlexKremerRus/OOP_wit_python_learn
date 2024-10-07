class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print("Incorrect password")
            return None
        elif amountToDeposit <= 0:
            print("Invalid amount")
            return None
        else:
            self.balance = self.balance + amountToDeposit
            print("Amount deposited successfully")
            return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print("Incorrect password")
            return None

        elif amountToWithdraw <= 0:
            print("Invalid amount")
            return None

        elif amountToWithdraw > self.balance:
            print("Insufficient balance")
            return None

        else:
            self.balance = self.balance - amountToWithdraw
            print("Amount withdrawn successfully")
            return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("Incorrect password")
            return None
        print("Balance:", self.balance)
        return self.balance

    def show(self):
        print('       Name:', self.name)
        print('       Balance:', self.balance)
        print('       Password:', self.password)
        print()
Alex_Bank_Account = Account("Alex Bank Account", 1000, '1234')

Alex_Bank_Account.show()
print('----------------------------------')

Alex_Bank_Account.getBalance('1234')
print('----------------------------------')

Alex_Bank_Account.deposit(500, "1234")
print('----------------------------------')

Alex_Bank_Account.getBalance("1234")
print('----------------------------------')

Alex_Bank_Account.deposit(500, "12342")
print('----------------------------------')

Alex_Bank_Account.withdraw(1000, "1234")
print('----------------------------------')

Alex_Bank_Account.getBalance("1234")
print('----------------------------------')

Alex_Bank_Account.show()
