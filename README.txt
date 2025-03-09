README.txt

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. processing.py (Driver File): This is the driver file of PyBank, which contains the user and backend classes, enabling for the backend processing of creating accounts, deposits, withdrawals, viewing credut scores, and transferring money between accounts. We also have a secret "admin" mode, which provides access to the user database, hidden behind the user.
2. ui.py: The frontend of PyBank. Includes six options for user to navigate across to perform the functions mentioned above.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Blueprint of Classes:

Class User:
- __init__(self, name, balance, debt, cscore)
- withdraw(self, withdrawal)
- deposit(self, deposit)
- view_cscore(self)
- transfer(self)

Class Backend:
- __init__(self, fname)
- save(self)
- load_user(self, uname)
- create_user(self, uname)
- depositer(self)
- withdrawer(self)
- cscore_viewer(self)
- transfer_money(self)

Here's more information about each class and their functions.

class User:

name: Name of user
balance: Balance of user’s account. 
debt: Debt owed by user. 
cscore: Credit score of user.

Methods:

__init__(self, name: str, balance: float, debt: float, cscore: float) -> None:
Initialization of class attributes.

withdraw(self, withdrawal: float) -> None:
Allows for withdrawal of the amount passed in function header from bankn account. If balance is lesser than withdrawal, the debt adds up, along with credit score going down. 

deposit(self, deposit: float) -> None:
Allows user to deposit the amount passed in function header to bank account. Credit score also increases depending on the amount of money deposited. 

view_cscore(self) -> float:
Returns current credit score of the user. 

transfer(self) -> bool:
Facilitates checks to ensure transaction takes place, and contains code for transfer.

class Backend:
userdb: Dictionary storing userdata, with the username acting as a key, with the information stored as values. 
fname: Name of file which stores user data. 

Methods:

__init__(self, fname = “Bankusers.txt”) -> None:
Initialization of class attributes. 

save(self) -> None:
Saves users data to file “Bankusers.txt”

load_user(self) -> dict:
Loads information for each user in PyBank.

create_user(self, uname: str) -> None:
Creates new user with relevant information, and is added to userdb. 

depositer(self) -> None:
Enables user to deposit money into existing account.

withdrawer(self) -> None:
Enables user to withdraw money from existing account.

cscore_viewer(self) -> None:
Enables user to view their banking information.

transfer_money(self) -> None:
Allows transfer of money between accounts by taking in name of sender and recipient.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Text file:
Bankusers.txt - Text file which stores user banking information. 

Dictionary:
userdb - Key: Username, Values: List containing balance, debt, and credit score.  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Prototypes of all functions with documentation:

1.
# The function initializes the User class attributes.
# name: str - The name of the user.
# balance: float - The initial balance of the user.
# debt: float - The initial debt amount of the user.
# cscore: float - The initial credit score of the user.
# The function does not return any value.
def __init__(self, name: str, balance: float, debt: float, cscore: float) -> None:


2.
#This function allows users to withdraw money from their balance
#The withdrawal float is the amount to be withdrawn
#If there is not enough money, the amount is added to debt 
#Does not return any value

def withdraw(self, withdrawal: float) -> None:


3.
#This function allows users to deposit money into their bank account Yippee :D
#Deposit float is the amount to be deposited
#The function increases the bank balance and credit score pertaining to the amount deposited
#The function does not return any value

def deposit(self, deposit: float) -> None:


4. 
#The function returns the current credit score of the user
#returns the user's score as a float

view_cscore(self) -> float:

5.
#This function controls how money transfer takes place
#returns a boolean value depending on whether if transfer requirements are satisfied

def transfer(self, amount: float, recipient: str) -> bool:


6. 
#The function initializes the Backend class
#fname: the name of the file where user data is stored. str
#does not return any value

def __init__(self, fname = "Bankusers.txt") -> None:


7. 
#This function saves changes in the file. 
#This function does not return any value

def save(self) -> None:


8. 
#The function loads all user data stored in Bankusers.txt
#uname: str that holds the username of the user
#Function does not return any value

def load_user(self,uname:str) -> None:


9. 
#The function creates a new user and stores their data in the dictionary
#uname: str - username of new user

def create_user(self, uname:str) -> None:


10. 
#This function allows a user to deposit money into their bank account
#Does not return any value

def depositer(self) -> None:


11. 
#This function allows a user to withdraw money from their bank account
#Doesn't return any value

def withdrawer(self) -> None:


12. 
#This function displays credit score of the user's account
#This function does not return any value

def cscore_viewer(self) -> None:

13.
#This function takes in snder and recipient name, and calls the transfer function between those two accounts
#does not return any value

def transfer_money(self) -> None:



Prototypes of Functions:

Class User:
- __init__(self, name, balance, debt, cscore)
- withdraw(self, withdrawal)
- deposit(self, deposit)
- view_cscore(self)
- transfer(self, amount: float, recipient: str)

Class Backend:
- __init__(self, fname)
- save(self)
- load_user(self, uname)
- create_user(self, uname)
- depositer(self)
- withdrawer(self)
- cscore_viewer(self)
- transfer_money(self)


Bankusers.txt
{
'username': User(balance,debt,credit_score)
}