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
        #Saves all user data into the file
        with open(self.fname, 'w+') as fw:
            for user in self.userdb.values():
                fw.write(f"{user.name},{user.balance},{user.debt},{user.cscore}\n")
    # Vishal Murali Kannan
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
    # Vishal Murali Kannan
    # The function creates a new user and stores their data in the dictionary
    def create_user(self, uname: str, balance: float) -> str:
        if uname in self.userdb:
            return f"Account {uname} already exists!"
        if balance <= 0:
            raise ValueError("Initial deposit must be greater than 0.")
        debt, cscore = 0, 700 #default debt score for new users
        self.userdb[uname] = User(uname, balance, debt, cscore)
        return f"Account for {uname} created successfully."

    # Vishal Murali Kannan
    # This function allows a user to deposit money into their bank account
    def depositer(self, uname: str, amount: float) -> None:
        if uname not in self.userdb:
            raise ValueError(f"Account {uname} not found.")  # Sebastian Williams (Value errors)

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.userdb[uname].deposit(amount)


    # Vishal Murali Kannan
    # Value errors (Sebastian W)
    # This function allows a user to withdraw money from their bank account
    def withdrawer(self, uname: str, amount:float) -> None:
        if uname not in self.userdb:
            raise ValueError(f"Account {uname} not found.")
        if amount <=0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        self.userdb[uname].withdraw(amount)

    # Vishal Murali Kannan
    # Value errors added (Sebastian W)
    # This function displays credit score of the user's account
    def cscore_viewer(self, uname: str) -> float:
        if uname not in self.userdb:
            raise ValueError(f"Account {uname} not found.")
        return self.userdb[uname].view_cscore()

    # Vishal Murali Kannan
    # Value errors added - Sebastian W
    # This function takes in sender and recipient name, and calls the transfer function between those two accounts
    def transfer_money(self, sender: str, recipient: str, amount: float) -> str:
        if sender not in self.userdb or recipient not in self.userdb:
            raise ValueError(f"Sender {sender}'s account not found.")
        if recipient not in self.userdb:
            raise ValueError(f"Recipient {recipient}'s account not found.")
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than 0.")
        sender_account = self.userdb[sender]
        recipient_account = self.userdb[recipient]
        if sender_account.transfer(amount,recipient_account):
            self.save()
            return f"Transfer of {amount} from {sender} to {recipient} successful!"
        else:
            raise ValueError("Transfer failed. Insufficient funds. Get your money up, not your funny up fr :/")




