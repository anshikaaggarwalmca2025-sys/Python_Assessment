# Inventory management system using dictionary

# Empty inventory dictionary
inventory = {}

while True:

    print("\n===== INVENTORY MENU =====")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Display Low Stock Items")
    print("5. Exit")

    # User choice
    choice = int(input("Enter your choice: "))

    # Add product
    if choice == 1:

        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product_name] = quantity

        print("Product Added Successfully")

    # Update quantity
    elif choice == 2:

        product_name = input("Enter product name: ")

        if product_name in inventory:

            quantity = int(input("Enter new quantity: "))
            inventory[product_name] = quantity

            print("Quantity Updated")

        else:
            print("Product Not Found")

    # Search product
    elif choice == 3:

        product_name = input("Enter product name: ")

        if product_name in inventory:
            print("Available Quantity:", inventory[product_name])

        else:
            print("Product Not Found")

    # Display low stock items
    elif choice == 4:

        print("\nLow Stock Items:")

        for product, quantity in inventory.items():

            if quantity < 5:
                print(product, ":", quantity)

    # Exit
    elif choice == 5:

        print("Exiting Program...")
        break

    # Invalid choice
    else:

        print("Invalid Choice")


#output:
===== INVENTORY MENU =====
1. Add Product
2. Update Quantity
3. Search Product
4. Display Low Stock Items
5. Exit

Enter your choice: 1
Enter product name: Laptop
Enter quantity: 3

Product Added Successfully        