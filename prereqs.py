from sys import float_repr_style
# Sebastian Williams and Vishal Murali Kannan
class User:
    #Sebastian Williams
    # The function initializes the User class attributes
    # name: str - The name of the user
    # balance: float - The initial balance of the user
    # debt: float - The initial debt amount of the user
    # cscore: float - The initial credit score of the user
    def __init__(self, name: str, bal: float, debt: float, cscore: float) -> None:
        self.name = name
        self.balance = bal
        self.debt = debt
        self.cscore = cscore

    # This function allows users to withdraw money from their balance
    # The withdrawal float is the amount to be withdrawn
    # If there is not enough money, the amount is added to debt
    def withdraw(self, withdrawal: float) -> None:
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

    # This function allows users to deposit money into their bank account
    # Deposit float is the amount to be deposited
    # The function increases the bank balance and credit score pertaining to the amount deposited
    def deposit(self, deposit: float) -> None:
        if deposit <= 0:
            print("Enter a valid deposit amount.")
            return
        self.balance += deposit
        self.cscore += 0.003 * deposit
        print("Deposit successful. New Balance: {}".format(self.balance))

    # The function returns the current credit score of the user
    def view_cscore(self) -> float:
        return self.cscore

    # Vishal Murali Kannan
    # This function controls the process of transferring funds, based on 3 conditions:
    # 1. When transfer amount = 0
    # 2. When balance (including debt) does not cover the transfer
    # 3. When amount is greater than bank balance, but excluding debt
    def transfer(self, amount: float, recipient: str) -> bool:
        if amount <= 0:
            print("Transfer amount must be greater than 0.")
            return False
        if self.balance + self.debt < amount:
            print("Insufficient funds for transfer!")
            return False
        if amount > self.balance:
            extra = amount - self.balance
            self.debt += extra
            self.balance = 0
        else:
            self.balance -= amount
        recipient.balance += amount
        return True

# Vishal Murali Kannan
class Backend:
    # The function initializes the Backend class
    # fname: the name of the file where user data is stored.
    def __init__(self, fname='Bankusers.txt') -> None:
        self.userdb = {}
        self.fname = fname
        self.load_user()

    # This function saves changes in the file.
    def save(self) -> None:
        with open(self.fname, 'w+') as fw:
            for user in self.userdb.values():
                fw.write(f"{user.name},{user.balance},{user.debt},{user.cscore}\n")

    # The function loads all user data stored in Bankusers.txt
    def load_user(self) -> dict:
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

    # The function creates a new user and stores their data in the dictionary
    def create_user(self, uname: str) -> None:
        if uname in self.userdb:
            print("Account {} already exists!".format(uname))
            return
        balance = float(input("Enter balance to deposit: "))
        debt, cscore = 0, 700
        self.userdb[uname] = User(uname, balance, debt, cscore)
        print("Account for {} created.".format(uname))

    # This function allows a user to deposit money into their bank account
    def depositer(self) -> None:
        uname = input("Enter account holder name to deposit money in: ")
        if uname in self.userdb:
            dep = float(input("Enter amount to deposit: "))
            self.userdb[uname].deposit(dep)
        else:
            print("Account not found.")

    # This function allows a user to withdraw money from their bank account
    def withdrawer(self) -> None:
        uname = input("Enter account holder name to withdraw money from: ")
        if uname in self.userdb:
            witd = float(input("Enter amount to withdraw: "))
            self.userdb[uname].withdraw(witd)
        else:
            print("Account not found.")

    # This function displays credit score of the user's account
    def cscore_viewer(self) -> None:
        uname = input("Enter account holder name to view credit score: ")
        if uname in self.userdb:
            print("{}'s credit score: {}".format(uname, self.userdb[uname].view_cscore()))
        else:
            print("Account not found.")

    # This function takes in sender and recipient name, and calls the transfer function between those two accounts
    def transfer_money(self) -> None:
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
            if sinfo.transfer(amount, rinfo):
                print("Transfer of {} from {} to {} successful!".format(amount, sender, recipient))
        except ValueError:
            print("Invalid amount entered.")


