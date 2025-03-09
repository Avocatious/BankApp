import random
import time


# Spin the wheel animation
def spin_wheel_animation():
    print("Spinning the wheel...", end="", flush=True)
    outcomes = ["***", "BIG WIN!!!", "***", "You lost...", "***", "***",
                "You doubled your money!", "***", "***", "NICE!"]

    # Simulate spinning wheel animation
    for _ in range(10):
        print(f"{random.choice(outcomes)}", end="\r", flush=True)  # Display random outcomes
        time.sleep(0.2)  # Wait for animation
        print(" " * 30, end="\r")  # Clear previous text

    # Return final spinning result
    result = random.choice(outcomes)
    print(f"Final Result: {result}\n")
    return result


# Main game controller
def handle_lottery_game(backend):
    # Game loop
    from ui import get_input

    while True:
        uname = get_input("Enter your account name: ")
        if uname is None:
            return
        if uname not in backend.userdb:
            print(f"Error. Account '{uname}' does not exist!")
            continue
        user = backend.userdb[uname]
        if user.balance < 10:
            print("Insufficient funds. $10 minimum buy-in.")
            return
        print(f"\nWelcome to the Lottery, {uname}!")
        print(f"Your starting balance is ${user.balance:.2f}.\n")
        print("Each spin costs $10. You may win or lose money depending on the outcome.")

        while True:
            # Display the lottery game menu
            print("\nLottery Game Menu:")
            print("1. Spin the Wheel")
            print("2. Show Rules")
            print("0. Exit to Main Menu")

            user_choice = input("\nEnter your choice: ").strip()

            if user_choice == "1":  # Spin the wheel
                if user.balance < 10:
                    print("Insufficient funds to spin! You need at least $10.")
                    return  # Exit back to the main PyBank menu

                # Deduct cost of spinning the wheel
                user.balance -= 10
                backend.save()
                print("Spinning the wheel!")

                result = spin_wheel_animation()

                # Process the spin result and adjust the balance accordingly
                if result == "BIG WIN!!!":
                    user.balance += 500  # A huge jackpot win!
                    print(f"Congratulations, {uname}! You won $500! Your new balance is ${user.balance:.2f}.")
                elif result == "You doubled your money!":
                    user.balance += 20  # Net +20 because spin cost 10
                    print(f"Wow, {uname}! You doubled your money! Your new balance is ${user.balance:.2f}.")
                elif result == "You lost...":
                    print(f"Sorry, {uname}, you lost this round. Your balance is now ${user.balance:.2f}.")
                else:  # Neutral spin
                    print(f"Neutral spin, {uname}. Your balance remains at ${user.balance:.2f}.")

                # Save the updated balance after every spin
                backend.save()

            elif user_choice == "2":  # Show rules
                print("\nRules of the Lottery Game:")
                print("1. Each spin costs $10 to play.")
                print("2. Possible outcomes:")
                print("   - 'BIG WIN!!!' earns you $500.")
                print("   - 'You doubled your money!' gives you $20 (net profit $10).")
                print("   - 'You lost...' deducts $10 (the spin cost).")
                print("   - 'Neutral spin' has no effect on your balance.")
                print("3. You must have a minimum balance of $10 to participate.")

            elif user_choice == "0":  # Exit the lottery game
                print(f"\nGoodbye, {uname}! Returning to the main menu...")
                return  # Exit to main PyBank menu

            else:
                print("\nInvalid choice. Please try again.")
if __name__ == "__main__+":

# Run the game
    handle_lottery_game()
