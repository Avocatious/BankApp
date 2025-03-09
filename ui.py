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
                uname = get_input("Enter account holder name: ")
                if uname is None:
                    continue
                try:
                    balance = float(get_input("Enter initial deposit amount: "))
                    if balance <= 0:
                        print("Initial deposit must be greater than 0. Please try again.")
                        continue
                    response = backend.create_user(uname, balance)
                    backend.save()
                    print(f"Account for {uname} successfully created!\n")
                except ValueError:
                    print("Invalid input. Make sure to enter a valid number for the balance.")
                except Exception as e:
                    print(f"Unexpected error: {e}")

            #Sebastian Williams
            elif choice in ['2', 'deposit money']:
                uname = get_input("Enter account holder name to deposit money: ")
                if uname is None:
                    continue
                try:
                    dep = float(get_input("Enter deposit amount: "))
                    if dep <= 0:
                        print("Deposit amount must be greater than 0. Please try again.")
                        continue

                    backend.depositer(uname, dep)
                    backend.save()
                    print(f"Deposit of {dep} successful.\n""New Balance:"
                    f"{backend.userdb[uname].balance}")
                except ValueError as e:
                    print(e)
                except Exception as e:
                    print(e)

            #Sebastian Williams
            elif choice in ['3', 'withdraw money']:
                uname = get_input("Enter account holder name to withdraw money: ")
                if uname is None:
                    continue
                withdraw = get_input("Enter amount to withdraw: ")
                if withdraw is None:
                    continue
                try:
                    backend.withdrawer(uname, float(withdraw))
                    backend.save()
                    print(f"Withdrawal successful. New Balance: {backend.userdb[uname].balance}")
                except ValueError:
                    print("You can't deposit this amount.")
                except Exception as e:
                    print(e)


            #Sebastian Williams
            elif choice in ['4', 'view credit score']:
                uname = get_input("Enter account holder name to view credit score: ")
                if uname is None:
                    continue
                backend.cscore_viewer(uname)
                try:
                    score = backend.cscore_viewer(uname)
                    print(f"{uname}'s Credit Score: {score}")
                except ValueError as e:
                    print(e)
                except Exception as e:
                    print(e)
            #Sebastian Williams
            elif choice in ['5', 'transfer money']:
                sender = get_input("Enter the account you wish to transfer money from: ")
                if sender is None:
                    continue
                recipient = get_input("Enter recipient's account name: ")
                if recipient is None:
                    continue
                amount = get_input("Enter amount to transfer: ")
                if amount is None:
                    continue
                try:
                    backend.transfer_money(sender, recipient, float(amount))
                    backend.save()
                    print(f"{amount} successfully transfered from {sender} to {recipient}!")
                except ValueError as e:
                    print(e)
                except Exception as e:
                    print(e)

            elif choice in ['6', 'exit']:
                print("Thank you for using PyBank! Shutting down...")
                break

            #Vishal Murali Kannan
            elif choice.lower() == 'admin':
                db = backend.load_user()
                if db:
                    for uname, user in db.items():
                        print("User: {}, Balance: {}, Debt: {}, Credit Score: {}".format(uname, user.balance, user.debt, user.cscore))
                else:
                    print("Empty Database.")
            else:
                print("Invalid choice. Input can only be a number from 1 through 6.")
        except ValueError:
            print("Invalid input. Please enter a valid selection.")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()