# ATM simulation program with PIN validation

# Correct PIN
correct_pin = "1234"

# Maximum attempts
attempts = 0

# Loop for PIN verification
while attempts < 3:

    # User input
    entered_pin = input("Enter ATM PIN: ")

    # Check PIN
    if entered_pin == correct_pin:

        print("PIN Verified Successfully")
        print("Welcome to ATM")

        break

    else:

        attempts += 1

        print("Incorrect PIN")

        remaining_attempts = 3 - attempts

        print("Remaining Attempts:", remaining_attempts)

# Lock account after 3 invalid attempts
if attempts == 3:

    print("Account Locked Due to Multiple Invalid Attempts")


#output:
Enter ATM PIN: 1111
Incorrect PIN
Remaining Attempts: 2

Enter ATM PIN: 2222
Incorrect PIN
Remaining Attempts: 1

Enter ATM PIN: 3333
Incorrect PIN
Remaining Attempts: 0

Account Locked Due to Multiple Invalid Attempts    