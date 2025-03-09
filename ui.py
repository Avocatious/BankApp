from prereqs import User, Backend
#boo!
def main():
    backend = Backend()
    while True:
        print("Welcome to PyBank!:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Credit Score")
        print("5. Transfer Money")
        print("6. Exit")
        choice = input("What would you like to do today? (Choose a number): ")

        if choice == '1':
            uname = input("Enter account holder name: ")
            backend.create_user(uname)
            backend.save()
        elif choice == '2':
            backend.depositer()
            backend.save()
        elif choice == '3':
            backend.withdrawer()
            backend.save()
        elif choice == '4':
            backend.cscore_viewer()
        elif choice == '5':
            backend.transfer_money()
            backend.save()
        elif choice == '6':
            print("Thank you for using PyBank!")
            break
        elif choice.lower() == 'admin':
            db = backend.load_user()
            if db:
                for uname, user in db.items():
                    print("User: {}, Balance: {}, Debt: {}, Credit Score: {}".format(uname, user.balance, user.debt, user.cscore))
            else:
                print("Empty Database.")
        else:
            print("Invalid choice. Input can only be a number from 1 through 6.")


if __name__ == "__main__":
    main()