class BankAccount:
    def __init__(self, account_name, int_rate=0.004, balance=0):
        self.account_name = account_name
        self.int_rate = int_rate
        self.account_balance = balance
        
    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient Funds: Charging $5 fee")
            self.account_balance = self.account_balance - 5
        else:
            self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Current {self.account_name} Balance: {self.account_balance}")
        return self

    def yield_interest(self):
        # self.account_balance = self.account_balance * (1+self.int_rate)
        self.account_balance *= (1+self.int_rate)
        return self

#create instances of class BankAccount
checking = BankAccount('Checking',0.001)
savings = BankAccount('Savings',balance=1000)

#print beginning balances
print(f"Beginning Checking Balance: {checking.account_balance}")
print(f"Beginning Savings Balance: {savings.account_balance}")

#deposit/withdraw/yield interest/display account info
checking.deposit(100).deposit(100).deposit(100).withdraw(40).yield_interest().display_account_info()
savings.deposit(200).deposit(200).withdraw(30).withdraw(50).withdraw(90).withdraw(100).yield_interest().display_account_info()
