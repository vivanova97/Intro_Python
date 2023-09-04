class BankAccount():
    def __init__(self, account_number, balance = 0, number_of_operations = 0, interest_rate = 0.03):
        self.account_number = account_number
        self.balance = balance
        self.logged_in = False
        self.number_of_operations = number_of_operations
        self.interest_rate = interest_rate
    def log_in(self):
        self.logged_in = True
    def log_off(self):
        self.logged_in = False
    def deposit(self, amount):
        if amount %50 == 0:
            self.balance += amount
        else:
            print('Error! Amount should be a multiple of 50.')
        print(f'\nbalance: {self.balance}')
        self.number_of_operations += 1 
        if self.number_of_operations %3 == 0:
            self.balance += self.balance * self.interest_rate
            print(f'{self.balance * self.interest_rate} in interest deposited')
    def withdraw(self, amount):
        if amount <= self.balance and amount %50 ==0:
            self.balance -= amount
            if amount * 0.015 >= 30 and amount * 0.015 <= 600:
                self.balance -= amount * 0.015
                print(f'Interest for transaction: {amount * 0.015}')
            elif amount * 0.015 > 600:
                self.balance -= 600
                print(f'Interest for transaction: 600')
            elif amount * 0.015 < 30:
                self.balance -= 30
                print(f'Interest for transaction: 30')
            print(f'\nbalance: {self.balance}')
        else:
            print('Error! Insufficient funds or amount not a multiple of 50.')
        self.number_of_operations += 1
        if self.number_of_operations %3 == 0:
            self.balance += self.balance * self.interest_rate
            print(f'{self.balance * self.interest_rate} in interest deposited')
my_account = BankAccount(12345,0)





