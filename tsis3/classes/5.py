class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance =balance
    def deposit(self, money):
        self.balance += money
    def withdraw(self, money1):
        if(self.balance>= money1):
            self.balance -= money1
    def show(self):
        print(self.balance)

c=Account('Dina', 10000)
c.deposit(100)
c.show()
c.withdraw(500)
c.show()