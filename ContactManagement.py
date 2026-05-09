# Contact management system using dictionary

# Empty contacts dictionary
contacts = {}

while True:

    print("\n===== CONTACT MENU =====")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    # User choice
    choice = int(input("Enter your choice: "))

    # Add contact
    if choice == 1:

        name = input("Enter contact name: ")
        number = input("Enter phone number: ")

        contacts[name] = number

        print("Contact Added Successfully")

    # Update contact
    elif choice == 2:

        name = input("Enter contact name: ")

        if name in contacts:

            number = input("Enter new number: ")

            contacts[name] = number

            print("Contact Updated")

        else:
            print("Contact Not Found")

    # Search contact
    elif choice == 3:

        name = input("Enter contact name: ")

        if name in contacts:

            print("Phone Number:", contacts[name])

        else:
            print("Contact Not Found")

    # Delete contact
    elif choice == 4:

        name = input("Enter contact name: ")

        if name in contacts:

            del contacts[name]

            print("Contact Deleted")

        else:
            print("Contact Not Found")

    # Display all contacts
    elif choice == 5:

        print("\nAll Contacts:")

        for name, number in contacts.items():
            print(name, ":", number)

    # Exit
    elif choice == 6:

        print("Exiting Program...")
        break

    # Invalid choice
    else:

        print("Invalid Choice")


#output:
===== CONTACT MENU =====
1. Add Contact
2. Update Contact
3. Search Contact
4. Delete Contact
5. Display All Contacts
6. Exit

Enter your choice: 1
Enter contact name: Amit
Enter phone number: 9876543210

Contact Added Successfully        