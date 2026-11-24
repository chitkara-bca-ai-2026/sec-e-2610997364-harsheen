
print("===== INVENTORY CONTROL SYSTEM =====")

inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:

    print("\n----- MENU -----")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        print("\nCurrent Inventory:")
        for i in range(len(inventory)):
            print(f"{i+1}. {inventory[i]}")

    elif choice == 2:
        item = input("Enter item to add: ")
        inventory.append(item)
        print("Item added successfully!")

    elif choice == 3:
        item = input("Enter item to remove: ")

        if item in inventory:
            inventory.remove(item)
            print("Item removed successfully!")
        else:
            print("Item not found in inventory!")

    elif choice == 4:
        inventory.sort()
        print("\nInventory sorted alphabetically:")
        for i in range(len(inventory)):
            print(f"{i+1}. {inventory[i]}")

    elif choice == 5:
        print("Thank you! Exiting Inventory System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
