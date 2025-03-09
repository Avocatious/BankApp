from prereqs import User, Backend
#Sebastian Williams and Vishal Murali Kannan

# Sebastian Williams
# Allows users to return to menu at any point in using PyBank
def get_input(prompt:str):
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
        print("6. Exit")
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

            elif choice in ['6', 'exit']:
                print("Thank you for using PyBank! Shutting down...")
                break

            #Vishal Murali Kannan
            elif choice.lower() == 'admin':
              handle_admin_mode(backend)
            else:
                print("Invalid choice. Input can only be a number from 1 through 6.")
        except ValueError:
            print("Invalid input. Please enter a valid selection.")
        except Exception as e:
            print(f"Unexpected error: {e}")

def handle_create_account(backend):
    while True:
        try:
            uname = get_input("Enter account holder name: ")
            if uname is None:
                break
            balance = float(get_input("Enter initial deposit amount: "))
            response = backend.create_user(uname, balance)
            backend.save()
            print(f"Account for {uname} successfully created!")
            break
        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Unexpected error occurred: {e}")

def handle_deposit_money(backend):
    """Handle depositing money into an account."""
    while True:
        try:
            uname = get_input("Enter account holder name to deposit money: ")
            if uname is None:
                break

            dep = float(get_input("Enter deposit amount: "))
            backend.depositer(uname, dep)  # Backend handles validation
            backend.save()
            print(f"Deposit successful! New Balance: {backend.userdb[uname].balance}")
            break

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")

def handle_withdraw_money(backend):
    """Handle withdrawing money from an account."""
    while True:
        try:
            uname = get_input("Enter account holder name to withdraw money: ")
            if uname is None:
                break

            amount = float(get_input("Enter amount to withdraw: "))
            backend.withdrawer(uname, amount)  # Backend handles checks like sufficient funds
            backend.save()
            print(f"Withdrawal successful! New Balance: {backend.userdb[uname].balance}")
            break

        except ValueError as e:
            print(f"Error: {e}")  # Example: Insufficient funds
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
def handle_view_credit_score(backend):
    """Handle viewing the credit score of a user."""
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

def handle_transfer_money(backend):
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


def handle_admin_mode(backend):
    """Optional admin functionality to view all users in the database."""
    db = backend.load_user()
    if db:
        print("PyBank Users:")
        for uname, user in db.items():
            print(f"User: {uname}, Balance: {user.balance}, Debt: {user.debt}, Credit Score: {user.cscore}")
    else:
        print("Empty Database.")

if __name__ == "__main__":
    main()