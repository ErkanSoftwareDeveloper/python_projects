def atm():
    balance = 1000  # START BALANCE

    print("Welcome to the ATM")

    while True:
        print("\n1: Check Balance")
        print("2: Deposit Money")
        print("3: Withdraw Money")
        print("4: Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your balance is: {balance:.2f} TL")

        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Please enter a positive amount!")
                else:
                    balance += amount
                    print(f"New balance: {balance:.2f} TL")
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Please enter a positive amount!")
                elif amount > balance:
                    print("Not enough balance!")
                else:
                    balance -= amount
                    print(f"New balance: {balance:.2f} TL")
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-4.")


if __name__ == "__main__":
    atm()
