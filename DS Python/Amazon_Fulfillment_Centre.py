# Amazon Fulfillment Centre (Array)

belt = [None] * 8   # Conveyor belt with 8 slots

while True:
    print("\n--- Amazon Fulfillment Centre ---")
    print("1. Add/Update Product")
    print("2. Check Product at Slot")
    print("3. Find Product")
    print("4. Check if Belt is Full")
    print("5. Display Belt")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        slot = int(input("Enter slot number (0-7): "))
        if 0 <= slot <= 7:
            product = input("Enter product name: ")
            belt[slot] = product
            print("Product stored successfully.")
        else:
            print("Invalid slot!")

    elif choice == 2:
        slot = int(input("Enter slot number (0-7): "))
        if 0 <= slot <= 7:
            print("Product:", belt[slot])
        else:
            print("Invalid slot!")

    elif choice == 3:
        product = input("Enter product name to search: ")
        if product in belt:
            print("Found at slot:", belt.index(product))
        else:
            print("Product not found.")

    elif choice == 4:
        if None not in belt:
            print("Belt is FULL.")
        else:
            print("Belt is NOT FULL.")

    elif choice == 5:
        for i in range(8):
            print("Slot", i, ":", belt[i])

    elif choice == 6:
        break

    else:
        print("Invalid choice!")
