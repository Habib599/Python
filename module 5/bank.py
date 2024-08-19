
class Bank:
    def __init__(self, balance):
        self.balance = balance
        print(f'your balance is {self.balance}')
        self.min_withdraw = 100
        self.max_withdraw = self.balance
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposit {amount}')
            print(f'balance after deposit {self.get_balance()}')
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'you can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print (f'you can not withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'withdraw {amount}')
            print(f'balance after withdraw: {self.get_balance()}')

brac = Bank(15000)
brac.withdraw(200)
brac.withdraw(5000)
brac.withdraw(1000)
brac.deposit(6200)
brac.withdraw(10000000)