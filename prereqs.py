from sys import float_repr_style
#meow
class User:
    def __init__(self, name: str, bal: float, debt: float, cscore: float):
        self.name = name
        self.balance = bal
        self.debt = debt
        self.cscore = cscore

    def withdraw(self, withdrawal: float):
        if withdrawal > 0:
            print("Enter valid withdrawal amount.")
        else:
            for i in range(0, withdrawal):
                self.balance -= 1
                if self.balance == 0:
                    self.debt += 1
                    self.cscore -= 0.002 * withdrawal
            return "Balance: {}, Debt: {}".format(self.balance, self.debt)

    def deposit(self, deposit: float):
        for i in range(0, deposit):
            self.balance += 1
            self.cscore += 0.003 * deposit
        return "Balance: {}, Current Credit Score: {}".format(self.balance, self.cscore)

    def view_cscore(self):
        return self.cscore


class Backend:
    def __init__(self, fname = 'Bankusers.txt'):
        self.userdb = {}
        self.fname = fname
        self.load_user()

    def saving_users(self):
        with open(self.fname, 'w+') as fw:
            for user in self.userdb.values():
                fw.write(f"{user.name},{user.balance},{user.debt},{user.cscore}\n")
            print("User{} saved to {}.".format(User.name, self.fname))

    def load_user(self, uname):
        with open(self.fname, 'r') as fr:
            for line in fr.readlines():
                acc = line.strip().split(',')
                name = acc[0]
                if name == uname:
                    balance = float(acc[1])
                    debt = float(acc[2])
                    cscore = float(acc[3])
                    user = User(name, balance, debt, cscore)
                    self.userdb[name] = user
                    return user

    def create_user(self, uname):
        if uname in self.userdb:
            print(uname, "already exists!")
            return
        balance = float(input("Enter balance to deposit: "))
        debt, cscore = 0, 0
        self.userdb[uname] = User(uname, balance, debt, cscore)

    def depositer(self):
        uname = input("Enter account holder name to deposit money in: ")
        if uname in self.userdb:
            dep = float(input("Enter amount to deposit: "))
            self.userdb[uname].deposit(dep)
        else:
            print("Account not found.")

    def withdrawer(self):
        uname = input("Enter account holder name to withdraw money in: ")
        if uname in self.userdb:
            witd = float(input("Enter amount to withdraw: "))
            self.userdb[uname].withdraw(witd)
        else:
            print("Account not found.")

    def cscore_viewer(self):
        uname = input("Enter account holder name to view credit score: ")
        if uname in self.userdb:
            self.userdb[uname].cscore_viewer()
        else:
            print("Account not found.")

def main():
    backend = Backend()
    while True:
        print("*****Welcome to PyBank!*****")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Credit Score")
        print("6. Exit")
        opt = int(input("Choose an option: "))
        if opt == 1:
            uname = input("Enter Username: ")
            backend.create_user(uname)
        elif opt == 2:
            uname = input("Enter Username: ")
            backend.load_user(uname)
        elif opt == 3:
            backend.depositer()
        elif opt == 4:
            backend.withdrawer()
        elif opt == 5:
            backend.cscore_viewer()
        elif opt == 6:
            backend.saving_users()
        else:
            print("Enter valid option.")


