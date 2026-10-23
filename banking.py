balance = 10000

print("Welcome to Kiran Bank")
print("Opening Balance: ₹", balance)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Current Balance: ₹", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful.")
            print("Updated Balance: ₹", balance)
        else:
            print("Invalid amount. Deposit must be greater than 0.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount. Withdrawal must be greater than 0.")

        elif amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Updated Balance: ₹", balance)

        else:
            print("Transaction failed: Insufficient balance.")
            print("Current Balance: ₹", balance)

    elif choice == 4:
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 and 4.")