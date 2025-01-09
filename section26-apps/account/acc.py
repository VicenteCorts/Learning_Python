# Clase 236 -> aprendiendo más POO
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
            
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking account objects"""
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking("section26-apps/account/balance.txt", 1)
checking.transfer(100)
print(checking.balance)
checking.commit()
print(checking.__doc__)
'''
account = Account("section26-apps/account/balance.txt")
print(account.balance)

account.withdraw(100)
print(account.balance)

account.deposit(200)
print(account.balance)

account.commit()
'''