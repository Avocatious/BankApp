

class User:
    def __init__(self, bal: float, debt: float, cscore: float):
        self.balance = bal
        self.debt = debt
        self.credit_score = cscore

    def withdraw(self, withdrawal: float):
        if withdrawal > self.balance:
            self.debt += withdrawal - self.balance
            self.credit_score -= (withdrawal - self.balance) * 0.002
            self.balance = 0
        else:
            self.balance -= withdrawal

        return self

    def deposit(self, deposit:float):
        self.balance += deposit
        self.credit_score += deposit * 0.003
        return self

    def credit_check(self):
        return self.credit_score

    def createUser(self):
        uname = input("Enter Name of New Account Holder: ")
        bal = float(input("Enter Balance: "))
        debt, cscore = 0, 0
        user = User(bal, debt, cscore)
        users_dict[uname] = user

        with open("Bankusers.txt", "w+") as f:
            f.write(str(users_dict))

        f = open("Bankusers.txt", "w+")
        f.write(str(users_dict))
        f.close()

        print(f"User {uname}")


users_dict = {}

