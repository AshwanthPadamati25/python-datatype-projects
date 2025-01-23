class BankAccount:
    def __init__(self, account_number):
        self.account_number = str(account_number)
        self.balance = 0
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient Funds")
            
    def deposit(self, amount):
        self.balance += amount
        
    def get_balance(self):
        return self.balance
    
def transfer_amount(acc_1, acc_2, amount):
    try:
        acc_1.withdraw(amount)
        acc_2.deposit(amount)
        return True
    except ValueError as err:
        print(str(err))
        print(type(err))
        print(err.args)
        return False
    
    
    

user_1 = BankAccount("001")
user_2 = BankAccount("002")
user_1.deposit(25)
user_2.deposit(100)

print(transfer_amount(user_1, user_2, 50))

print(user_1.get_balance())
print(user_2.get_balance())