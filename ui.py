from Lottery_code import handle_lottery_game
from prereqs import User, Backend
#Sebastian Williams and Vishal Murali Kannan

# Sebastian Williams
# Allows users to return to menu at any point in using PyBank
def get_input(prompt:str) -> str:
    user_input = input(prompt)
    if user_input.lower() == 'menu':
        confirm = input("You are returning to menu. Your progres in this section will NOT be saved. Type 'yes' to continue or 'no' to stay: ")
        if confirm.lower() == 'yes':
            print("Returning to main menu...\n")
        return None
    return user_input
def main():
    # Sebastian Williams
    # instantiates Backend class from prereqs.py
    backend = Backend()

    while True:
        print("\nWelcome to PyBank!:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Credit Score")
        print("5. Transfer Money")
        print("6. Take out a loan")
        print("7. Exit")
        print("8. Super Secret Option")
        choice = get_input("What would you like to do today? Choose a number or type 'menu' at any point to return to menu: ")

        if choice is None:  # This will return user back to menu
            continue

        # Sebastian Williams
        # Executes functions from Backend based on user selection
        try:
            choice = choice.lower()

            if choice in ['1', 'create account']:
                handle_create_account(backend)

            #Sebastian Williams
            elif choice in ['2', 'deposit money']:
                handle_deposit_money(backend)

            #Sebastian Williams
            elif choice in ['3', 'withdraw money']:
                handle_withdraw_money(backend)

            #Sebastian Williams
            elif choice in ['4', 'view credit score']:
                handle_view_credit_score(backend)

            #Sebastian Williams
            elif choice in ['5', 'transfer money']:
                handle_transfer_money(backend)
            #SW
            elif choice in ['6', 'loan']:
                handle_request_loan(backend)
            #SW
            elif choice in ['7', 'exit']:
                print("Thank you for using PyBank! Shutting down...")
            #SW
            elif  choice in ['8', 'lottery']:
                handle_lottery_game(backend)

            #Vishal Murali Kannan
            elif choice.lower() == 'admin':
              handle_admin_mode(backend)
            else:
                print("Invalid choice. Input can only be a number from 1 through 6.")
        except ValueError:
            print("Invalid input. Please enter a valid selection.")
        except Exception as e:
            print(f"Unexpected error: {e}")

#Sebastian Williams
#This function handles errors in the ui  for creating accounts and references the backend functions
def handle_create_account(backend) -> None:
    while True:
        try:
            #Vishal Murali Kannan
            uname = get_input("Enter account holder name: ")
            if uname is None:
                break
            balance = float(get_input("Enter initial deposit amount: "))
            response = backend.create_user(uname, balance)
            backend.save()
            print("Account for {} successfully created!".format(uname))
            break
        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Unexpected error occurred: {e}")

#Sebastian Williams - try and except loops
#This fn handles errors with the deposit function from the backend
def handle_deposit_money(backend) -> None:
    while True:
        try:
            # Vishal Murali Kannan
            uname = get_input("Enter account holder name to deposit money: ")
            if uname is None:
                break

            dep = float(get_input("Enter deposit amount: "))
            backend.depositer(uname, dep)  # Backend handles validation
            backend.save()
            print("Deposit successful! New Balance: {}".format(backend.userdb[uname].balance))
            break



        except ValueError:
            print("Invalid deposit amount! Please enter a numeric value.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

#Sebastian Williams - try and except loops
#This function handles potential user errors in ui when withdrawing money from an account
def handle_withdraw_money(backend) -> None:
    while True:
        try:
            # Vishal Murali Kannan
            uname = get_input("Enter account holder name to withdraw money: ")
            if uname is None:
                break

            amount = float(get_input("Enter amount to withdraw: "))
            backend.withdrawer(uname, amount)
            backend.save()
            print("Withdrawal successful! New Balance: {}".format(backend.userdb[uname].balance))
            break

        except ValueError as e:
            print(f"Error: {e}")  # Example: Insufficient funds
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

#Sebastian Williams
#This fn handles potential errors a user makes in the ui whilst viewing credit score
def handle_view_credit_score(backend) -> None:
    while True:
        try:
            uname = get_input("Enter account holder name to view credit score: ")
            if uname is None:
                break

            score = backend.cscore_viewer(uname)  # Assume this returns the credit score
            print(f"{uname}'s Credit Score: {score}")
            break

        except ValueError as e:
            print(f"Error: {e}")  # Backend-provided error message
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

#Sebastian Williams
#This fn handles potential errors a user makes in the ui whilst transferring money
def handle_transfer_money(backend) -> None:
    """Handle transferring money between accounts."""
    while True:
        try:
            sender = get_input("Enter the account you wish to transfer money from: ")
            if sender is None:
                break

            recipient = get_input("Enter recipient's account name: ")
            if recipient is None:
                break

            amount = float(get_input("Enter amount to transfer: "))
            backend.transfer_money(sender, recipient, amount)
            backend.save()
            print(f"Transfer successful! {amount} successfully transferred from {sender} to {recipient}.")
            break

        except ValueError as e:
            print(f"Error: {e}")  # Example: Invalid account or insufficient funds
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

#Sebastian Williams
#This fn handles potential errors an admin makes in the ui whilst loading PyBank users
def handle_admin_mode(backend) -> None:
    db = backend.load_user()
    # Vishal Murali Kannan
    if db:
        print("PyBank Users:")
        for uname, user in db.items():
            print("User: {}, Balance: {}, Debt: {}, Credit Score: {}".format(uname, user.balance, user.debt, user.cscore))
    else:
        print("Empty Database.")

#Sebastian Williams
#This fn handles potential errors a user makes in the ui whilst taking out a loan
def handle_request_loan(backend) -> None:
    while True:
        try:
            uname = get_input("Enter your account name to request a loan: ")
            if uname is None:
                break

            if uname not in backend.userdb:
                print(f"Error: Account '{uname}' does not exist!")
            user = backend.userdb[uname]
            max_loan_factor = 100
            max_loan_allowed = user.cscore*max_loan_factor
            print(f"New balance: ${user.balance:.2f},"
                f"Total Debt: ${user.debt:.2f}, Credit Score: {user.cscore:.2f}")
            print(f"Based on your credit score, you can take out a maximum loan of: ${max_loan_allowed:.2f}")

            amount = float(get_input("Enter the  loan amount: "))
            if amount <=0:
                print("Loan amount must be greater than 0.")
                continue

            response = backend.request_loan(uname,amount)
            print(response)
            break

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()