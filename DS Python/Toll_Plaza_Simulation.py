# Circular Queue

SIZE = 5
queue = [None] * SIZE
front = -1
rear = -1

def enqueue(vehicle):
    global front, rear

    if (rear + 1) % SIZE == front:
        print("Queue is FULL!")
        return

    if front == -1:
        front = rear = 0
    else:
        rear = (rear + 1) % SIZE

    queue[rear] = vehicle
    print(vehicle, "entered.")

def dequeue():
    global front, rear

    if front == -1:
        print("Queue is EMPTY!")
        return

    print(queue[front], "left the toll.")

    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % SIZE

def display():
    global front, rear

    if front == -1:
        print("Queue is empty.")
        return

    print("Vehicles in Queue:")

    i = front
    while True:
        print(queue[i])
        if i == rear:
            break
        i = (i + 1) % SIZE

while True:
    print("\n--- Toll Plaza ---")
    print("1. Vehicle Enter")
    print("2. Vehicle Exit")
    print("3. Display Queue")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        v = input("Enter vehicle number: ")
        enqueue(v)

    elif ch == 2:
        dequeue()

    elif ch == 3:
        display()

    elif ch == 4:
        break

    else:
        print("Invalid choice.")
