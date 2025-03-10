import unittest
from unittest.mock import mock_open, patch
from prereqs import User, Backend

#Sebastian Williams and Vishal Murali Kannan
#Test cases for the backend function
class TestUser(unittest.TestCase):

#SW
#setting up the dummy user on which we perform our test cases
    def setUp(self):
        self.user = User(name="dummy", bal = 1000, debt = 100, cscore = 750)

#Sebastian Williams
#Determining if withdraw works
    def test_withdraw(self):
        """Withdrawing 500 so new balance is 500. debt remains unchanged"""
        """#Should say "Withdrawal Successful! Balance: 500, Debt: 100"""
        self.user.withdraw(500)
        self.assertEqual(self.user.balance,500)
        self.assertEqual(self.user.debt,100)

    def test_withdraw_2(self):
        """"Should put user into debt of 300 dollars"""
        self.user.withdraw(1200)
        self.assertEqual(self.user.balance,0)
        self.assertEqual(self.user.debt, 300)
        self.assertEqual(self.user.cscore, 747.6)

#Sebastian Williams
#Determining if the deposit works for both valid inputs and str
    def test_deposit_validInput(self):
        self.user.deposit(500)
        self.assertEqual(self.user.balance,1500)

    def test_deposit_typeErrors(self):
        with self.assertRaises(TypeError):
            self.user.deposit('meow')


#Sebastian Williams
#Can only really test if the cscore is there or not for the 'view cscore' function
#Cscore changes in other functions such as depositing or withdrawing money
    def test_viewcscore(self):
        self.assertEqual(self.user.view_cscore(),750)
        def test_withdraw_2(self):
            self.user.withdraw(1200)
            self.assertEqual(self.user.view_cscore(),747.6)

#Sebastian Williams
#Test function for transferring money
#Since the user is transferring within his deposit, the debt will remain the same as it was in the start
#The recipient should have the transfer added to their balance

    def test_transfer(self):
        recipient = User(name = "John Doe", bal = 10, debt = 0, cscore = 700)
        self.user.transfer(500,recipient)
        self.assertEqual(self.user.balance,500)
        self.assertEqual(recipient.balance, 510)
        self.assertEqual(self.user.debt,100)

    def test_transfer_2(self):
        recipient = User(name = "Vishal Murali Kannan", bal = 1000000, debt = 0, cscore = 1000000)
        self.user.transfer(1000000, recipient)
        self.assertEqual(self.user.balance,1000)
        self.assertEqual(recipient.balance, 1000000)
        self.assertEqual(self.user.debt,100)

#Sebastian Williams
#Setting up the backend class to make the test cases for
class TestBackend(unittest.TestCase):
    def setUp(self):
        self.backend = Backend()
        self.backend.userdb.clear()
    #Initializing the backend so that we can test it wahoo yippee meow :D
    def Backend_initialization(self):
        self.assertIsInstance(self.backend.userdb,dict)
        self.assertEqual(self.backend.fname,"Bankusers.txt")


#Sebastian Williams
#This test case tests to see if when the user create an account it actually works
#Cat has a million dabloons because that is just how it is. Cat is rich
    def test_create_user(self):
        result = self.backend.create_user("Cat", 1000000)
        self.assertIn("Cat", self.backend.userdb)
        self.assertEqual(result, 'Account for Cat created.')

    def test_create_user_ALREADYEXISTSNOOOOOO(self):

        self.backend.create_user("Cat", 100)
        result = self.backend.create_user("Cat", 1000000)
        self.assertEqual(result, 'Account Cat already exists!')

#Sebastian Williams
#Okay so this test case is for the withdrawer function.
#first case is pretty standard, withdraw money, takes money from balance
    def test_withdrawer(self):
        self.backend.create_user("Cat", 1000)
        self.backend.withdrawer("Cat", 500)

        self.assertEqual(self.backend.userdb["Cat"].balance, 500)
        self.assertEqual(self.backend.userdb["Cat"].cscore, 700 - (0.002*500))
#For this case, the user withdraws more than their balance, and they go into debt! Cscore should change as well
    def test_withdrawer_exceeds_balance(self):
        self.backend.create_user("Cat", 1000)
        self.backend.withdrawer("Cat",1200)
        self.assertEqual(self.backend.userdb["Cat"].balance, 0)
        self.assertEqual(self.backend.userdb["Cat"].debt, 200)
        #Cscore changes by the amount withdrawn times the cscore factor of 0.002
        self.assertEqual(self.backend.userdb["Cat"].cscore, 700- (0.002*1200))

    def test_transfer_money_insufficient_funds(self):
        self.backend.create_user("Sebastian", 1000)
        self.backend.create_user("Vishal", 500)
        with self.assertRaises(ValueError) as context:
            self.backend.transfer_money("Sebastian","Vishal",2000)
            self.assertEqual(str(context.exception),"Transfer failed. Insufficient funds. Get your money up, not your funny up fr :/")
#Sebastian Williams
#This test case is for taking out loans
#TC 1: insufficient funds. Scram!
    def test_request_loan(self):
        self.backend.create_user("Meow",1000)
        self.backend.userdb["Meow"].cscore = 250
        with self.assertRaises(ValueError) as context:
            self.backend.request_loan("Meow", 500)

        expected = "Loan Denied. You don't have good credit. Scram!"
        self.assertEqual(str(context.exception),expected)
#TC2:
    def test_request_loan_success(self):
        self.backend.create_user("Meow", 1000)
        self.backend.userdb["Meow"].cscore = 700
        result = self.backend.request_loan("Meow", 500)

        expected = ("Loan of $500.00 approved.\n"
                    "New balance: $1500.00,Total Debt: $500.00, Credit Score: 675.00")
        self.assertEqual(result, expected)

#Vishal Murali Kannan
#testing the load user function
    def test_load_user_success(self):
        # Mock data representing a CSV file with user information
        mock_data = "John Doe,1000,200,700\nJane Doe,1500,0,750\n"

        # Mock the open function to simulate reading from a file
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = self.backend.load_user()

        # Verify that the userdb is populated correctly
        self.assertEqual(len(result), 2)
        self.assertIn("John Doe", result)
        self.assertIn("Jane Doe", result)
        self.assertEqual(result["John Doe"].balance, 1000)
        self.assertEqual(result["Jane Doe"].debt, 0)
        self.assertEqual(result["Jane Doe"].cscore, 750)
#Vishal Murali Kannan
    def test_load_user_empty_file(self):
        # Simulate an empty file (no user data)
        mock_data = ""

        # Mock the open function to simulate reading from an empty file
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = self.backend.load_user()

        # Expect the userdb to remain empty since the file is empty.
        self.assertEqual(result, {})


