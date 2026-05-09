# Banking application using while loop

# Initial balance
balance = 0

while True:

    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    # User choice
    choice = int(input("Enter your choice: "))

    # Deposit operation
    if choice == 1:

        amount = float(input("Enter deposit amount: "))
        balance += amount

        print("Amount Deposited Successfully")

    # Withdraw operation
    elif choice == 2:

        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")

        else:
            print("Insufficient Balance")

    # Check balance
    elif choice == 3:

        print("Current Balance:", balance)

    # Exit program
    elif choice == 4:

        print("Thank You for Using Banking Application")
        break

    # Invalid choice
    else:

        print("Invalid Choice")


#output:
===== BANK MENU =====
1. Deposit
2. Withdraw
3. Check Balance
4. Exit

Enter your choice: 1
Enter deposit amount: 5000

Amount Deposited Successfully        