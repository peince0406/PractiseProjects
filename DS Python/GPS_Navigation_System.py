# GPS Navigation (Backtracking using Stacks)

back_stack = []
forward_stack = []
current = "Home"

while True:
    print("\nCurrent Location:", current)
    print("1. Visit New Place")
    print("2. Back")
    print("3. Forward")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        place = input("Enter new place: ")
        back_stack.append(current)
        current = place
        forward_stack.clear()

    elif choice == 2:
        if back_stack:
            forward_stack.append(current)
            current = back_stack.pop()
        else:
            print("No previous place.")

    elif choice == 3:
        if forward_stack:
            back_stack.append(current)
            current = forward_stack.pop()
        else:
            print("No forward place.")

    elif choice == 4:
        break

    else:
        print("Invalid choice.")
