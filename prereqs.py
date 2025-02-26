class User:
    def __init__(self, bal: float, debt: float, cscore: float):
        self.balance = bal
        self.debt = debt
        self.credit_score = cscore

    def withdraw(self, withdrawal: float):
        for i in range(0, withdrawal):
            self.balance -= 1
            if self.balance == 0:
                self.debt += 1
                self.credit_score -= 0.002
        return self

    def deposit(deposit: float):
        for i in range(0, deposit):
            self.balance += 1
            self.credit_score += 0.003
        return self

    def credit_check(self):
        return self.credit_score

    def createUser(self):
        uname = input("Enter Name of New Account Holder: ")
        bal = float(input("Enter Balance: "))
        debt, cscore = 0, 0
        user = User(bal, debt, cscore)
        users_dict[uname] = user
        fh = open("Bankusers.txt", "w+")
        fh.write(str(users_dict))
        fh.close()


users_dict = {}

