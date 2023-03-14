class bankAccount:
    balance = 0
    int_rate = 0.01
    all_accounts = []

    def __init__(self, int_rate, balance, account_name):
        self.balance = balance
        self.int_rate = int_rate
        self.account_name = account_name
        bankAccount.all_accounts.append(self)

    def deposit(self, amount):
        if amount < 0:
            print(
                f"Sorry {self.account_name}, you cannot deposit negative amounts")
        else:
            self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount < 0:
            print(
                f"Sorry {self.account_name}, you cannot withdraw negative amounts")
        elif amount > self.balance:
            self.balance = self.balance - 5
            print(
                f"Sorry {self.account_name}, you cannot withdraw more than your current balance. Chargin a $5 Fee")
        else:
            self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f"Your current balance is ${self.balance}")
        print(f"Your interest rate is {self.int_rate}%")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate + self.balance
        return self

    @classmethod
    def accounts(cls):
        print("Here are your accounts:")
        for account in cls.all_accounts:
            print(
                f"{account.account_name}: ${account.balance} | Interest Rate: {account.int_rate}%")
        return cls


account1 = bankAccount(0.01, 0, "Jared's Checkings")
account2 = bankAccount(0.01, 1000, "Jared's Savings")
account3 = bankAccount(0.01, 1000000, "Dojo's Checkings")
account4 = bankAccount(0.01, 5000000, "Dojo's Savings")

account1.deposit(5000).deposit(1000).deposit(2000).withdraw(
    3000).yield_interest().display_account_info()
account2.deposit(10000).deposit(2000).withdraw(750).withdraw(
    1000).withdraw(1500).withdraw(300).yield_interest().display_account_info()

account2.withdraw(-1000)
account3.deposit(-500)
account4.withdraw(900000000)

bankAccount.accounts()
