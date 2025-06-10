class Bank:
    def __init__(self, owner, balance = 0, withdrawal = 0):
        self.owner = owner
        self. balance = balance
        self.withdrawal = withdrawal

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Your balance is low. Cannot make the withdrawal of {amount}")
        else:
            self.balance -= amount
            self.withdrawal +=amount
            print(f"Amount of {amount} withdrawal successful")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")


    def total_withdrawal(self):
        print(f"You have withdrew total amount of {self.withdrawal}")


customer1 = Bank("Sherya",50000)
customer1.check_balance()
customer1.withdraw(30000)
customer1.check_balance()
customer1.total_withdrawal()
customer1.withdraw(40000)
