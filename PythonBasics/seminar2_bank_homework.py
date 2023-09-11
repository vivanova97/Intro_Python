import datetime 
class BankAccount():
    def __init__(self, account_number, balance = 0, number_of_operations = 0, interest_rate = 0.03):
        self.account_number = account_number
        self.balance = balance
        self.logged_in = False
        self.number_of_operations = number_of_operations
        self.interest_rate = interest_rate
        self.transaction_history = []
    def log_in(self):
        self.logged_in = True
    def log_off(self):
        self.logged_in = False
    def deposit(self, amount):
        if amount %50 == 0:
            self.balance += amount
            self.transaction_history.append(f'{datetime.date.today()}: +{amount} deposit')
        else:
            print('Error! Amount should be a multiple of 50.')
        print(f'\nbalance: {self.balance}')
        self.number_of_operations += 1 
        if self.number_of_operations %3 == 0:
            self.balance += self.balance * self.interest_rate
            print(f'{self.balance * self.interest_rate} in interest deposited')
            self.transaction_history.append(f'{datetime.date.today()}: +{self.balance * self.interest_rate} interest deposited')
    def withdraw(self, amount):
        if amount <= self.balance and amount %50 ==0:
            self.balance -= amount
            self.transaction_history.append(f'{datetime.date.today()}: -{amount} withdrawn')
            if amount * 0.015 >= 30 and amount * 0.015 <= 600:
                self.balance -= amount * 0.015
                print(f'Interest for transaction: {amount * 0.015}')
                self.transaction_history.append(f'{datetime.date.today()}: -{amount*0.015} in interest withdrawn')
            elif amount * 0.015 > 600:
                self.balance -= 600
                print(f'Interest for transaction: 600')
                self.transaction_history.append('-600 in interest withdrawn')
            elif amount * 0.015 < 30:
                self.balance -= 30
                print(f'Interest for transaction: 30')
                self.transaction_history.append(f'{datetime.date.today()}: -30 in interest withdrawn')
            print(f'\nbalance: {self.balance}')
        else:
            print('Error! Insufficient funds or amount not a multiple of 50.')
        self.number_of_operations += 1
        if self.number_of_operations %3 == 0:
            self.balance += self.balance * self.interest_rate
            print(f'{self.balance * self.interest_rate} in interest deposited')

my_account = BankAccount(12345,0)
my_account.deposit(1000)
my_account.withdraw(500)
my_account.deposit(3000)
my_account.withdraw(1500)
print(my_account.transaction_history)
