from sys import float_repr_style
# #meow
class User:
    def __init__(self, name: str, bal: float, debt: float, cscore: float):
        self.name = name
        self.balance = bal
        self.debt = debt
        self.cscore = cscore

    def withdraw(self, withdrawal: float):
        if withdrawal <= 0:
            print("Enter amount greater than 0.")
            return
        if withdrawal > self.balance:
            excess = withdrawal - self.balance
            self.debt += excess
            self.balance = 0
        else:
            self.balance -= withdrawal
        self.cscore -= 0.002 * withdrawal
        print("Withdrawal successful! Balance: {}, Debt: {}".format(self.balance, self.debt))

    def deposit(self, deposit: float):
        if deposit <= 0:
            print("Enter a valid deposit amount.")
            return
        self.balance += deposit
        self.cscore += 0.003 * deposit
        print("Deposit successful. New Balance: {}".format(self.balance))

    def view_cscore(self):
        return self.cscore

    def transfer(self, amount: float, recipient):
        if amount <= 0:
            print("Transfer amount must be greater than 0.")
            return False
        if self.balance + self.debt < amount:
            print("Insufficient funds for transfer!")
            return False
        #Transfer facilitation with debt
        if amount > self.balance:
            extra = amount - self.balance
            self.debt += extra
            self.balance = 0
        else:
            self.balance -= amount

        recipient.balance += amount
        return True


class Backend:
    def __init__(self, fname='Bankusers.txt'):
        self.userdb = {}
        self.fname = fname
        self.load_user()

    def save(self):
        with open(self.fname, 'w+') as fw:
            for user in self.userdb.values():
                fw.write(f"{user.name},{user.balance},{user.debt},{user.cscore}\n")

    def load_user(self):
        try:
            with open(self.fname, 'r') as fh:
                for line in fh.readlines():
                    acc = line.strip().split(',')
                    name = acc[0]
                    balance = float(acc[1])
                    debt = float(acc[2])
                    cscore = float(acc[3])
                    user = User(name, balance, debt, cscore)
                    self.userdb[name] = user
            print("*****************PyBank Customers*****************")
            return self.userdb
        except FileNotFoundError:
            print("Database not found.")

    def create_user(self, uname):
        if uname in self.userdb:
            print("Account {} already exists!".format(uname))
            return
        balance = float(input("Enter balance to deposit: "))
        debt, cscore = 0, 700
        self.userdb[uname] = User(uname, balance, debt, cscore)
        print("Account for {} created.".format(uname))

    def depositer(self):
        uname = input("Enter account holder name to deposit money in: ")
        if uname in self.userdb:
            dep = float(input("Enter amount to deposit: "))
            self.userdb[uname].deposit(dep)
        else:
            print("Account not found.")

    def withdrawer(self):
        uname = input("Enter account holder name to withdraw money from: ")
        if uname in self.userdb:
            witd = float(input("Enter amount to withdraw: "))
            self.userdb[uname].withdraw(witd)
        else:
            print("Account not found.")

    def cscore_viewer(self):
        uname = input("Enter account holder name to view credit score: ")
        if uname in self.userdb:
            print("{}'s credit score: {}".format(uname, self.userdb[uname].view_cscore()))
        else:
            print("Account not found.")

    def transfer_money(self):
        sender = input("Enter sender's account name: ")
        recipient  = input("Enter recipient's account name: ")
        if sender not in self.userdb or recipient not in self.userdb:
            print("Either name does not exist in PyBank.")
            return
        sinfo = self.userdb[sender]
        rinfo = self.userdb[recipient]
        try:
            amount = float(input("Enter the amount to transfer: "))
            if amount <= 0:
                print("The amount must be greater than 0.")
                return
            if sinfo.transfer(amount, rinfo) == True:
                print("Transfer of {} from {} to {} successful!".format(amount, sender, recipient))
        except ValueError:
            print("Invalid amount entered.")


