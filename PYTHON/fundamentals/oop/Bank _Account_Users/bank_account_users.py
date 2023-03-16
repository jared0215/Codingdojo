class bankAccount:
    balance = 0
    int_rate = 0.01
    all_accounts = []

    def __init__(self, int_rate, balance,):
        self.balance = balance
        self.int_rate = int_rate
        bankAccount.all_accounts.append(self)

    def deposit(self, amount):
        if amount < 0:
            print(
                f"Sorry, you cannot deposit negative amounts")
        else:
            self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount < 0:
            print(
                f"Sorry, you cannot withdraw negative amounts")
        elif amount > self.balance:
            self.balance = self.balance - 5
            print(
                f"Sorry, you cannot withdraw more than your current balance. Chargin a $5 Fee")
        else:
            self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f"Your current balance is ${self.balance}")
        print(f"Your interest rate is {self.int_rate}%")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    all_users = [

    ]

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.all_users.append(self)
        self.accounts = {
            'checkings': bankAccount(int_rate=0.01, balance=0),
            'savings': bankAccount(int_rate=0.01, balance=0)
        }

    def make_deposit(self, amount, account_type, suppress_print=False):
        self.accounts[account_type].deposit(amount)
        if not suppress_print:
            print(f"{self.name} has deposited ${amount} into {account_type}")
        return self

    def make_withdraw(self, amount, account_type, suppress_print=False):
        self.accounts[account_type].withdraw(amount)
        if not suppress_print:
            print(f"{self.name} has withdrawn ${amount}")
        return self

    def display_user_balance(self, account_type):
        print(f"{self.name}, here is your {account_type} balance")
        self.accounts[account_type].display_account_info()
        print("\n")
        return self

    def yield_interest(self, account_type):
        self.accounts[account_type].yield_interest()
        return self

    def newBankAccount(self, account_type, amount=bankAccount.balance):
        self.accounts[account_type] = bankAccount(
            int_rate=0.01, balance=amount)
        print(f"{self.name} has created a new {account_type}")
        print("\n")
        return self

    def transfer_money(self, amount, account_from, account_to):
        self.make_withdraw(amount, account_from, suppress_print=True)
        self.make_deposit(amount, account_to, suppress_print=True)
        print(
            f"{self.name} has transferred ${amount} from {account_from} to {account_to}")
        print("\n")
        return self

    @staticmethod
    def user_transfer_money(amount, from_user, to_user, account_type_from, account_type_to):
        if from_user.accounts[account_type_from].balance >= amount:
            to_user.make_deposit(amount, account_type_to, suppress_print=True)
            from_user.make_withdraw(
                amount, account_type_from, suppress_print=True)
            print(
                f"{from_user.name} has transferred ${amount} from {account_type_from} to {to_user.name}s {account_type_to}")
        else:
            print("Sorry, you cannot transfer more than your current balance")
        print("\n")
        return to_user, from_user


jared = User('Jared', 'anpch@example.com')
jane = User('Jane', 'hzdkv@example.com')
john = User('John', 'hzdkv@example.com')

jared.newBankAccount('checkings', 5000).newBankAccount('savings')
jane.newBankAccount('checkings').newBankAccount('savings')
john.newBankAccount('checkings').newBankAccount('savings')


jared.display_user_balance('checkings').display_user_balance('savings')
jane.display_user_balance('checkings').display_user_balance('savings')

# jared.transfer_money(2000, 'checkings', 'savings')
jared.user_transfer_money(1000, jared, jane, 'checkings', 'savings')

jared.display_user_balance('checkings').display_user_balance('savings')
jane.display_user_balance('checkings').display_user_balance('savings')
