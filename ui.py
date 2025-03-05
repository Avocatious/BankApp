from prereqs import User, Backend
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
if __name__ == "__main__":
    main()