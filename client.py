import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9999))

running = True

while running:

    msg = s.recv(9999)
    print(msg.decode("utf-8"))

    print("""Python DB Menu
    
    1. Find customer
    2. Add customer
    3. Delete customer
    4. Update customer age
    5. Update customer address
    6. Update customer phone
    7. Print report
    8. Exit
    """)

    entry = input("Select: ")

    s.send(bytes(entry, "utf-8"))

    if entry == "1":
        name = input("Customer Name: ")
        s.send(bytes(name, "utf-8"))
        data = s.recv(9999)
        print("Server response: ")
        print(data.decode("utf-8"))

    elif entry == "2":
        print("Please enter the customer's info...")
        name = input("Customer Name: ")
        s.send(bytes(name, "utf-8"))
        age = input("Age: ")
        s.send(bytes(age, "utf-8"))
        addr = input("Address: ")
        s.send(bytes(addr, "utf-8"))
        num = input("Phone Number: ")
        s.send(bytes(num, "utf-8"))
        data = s.recv(9999)
        print("Server response: ")
        print(data.decode("utf-8"))

    elif entry == "3":
        name = input("Customer Name: ")
        s.send(bytes(name, "utf-8"))
        data = s.recv(9999)
        print("Server response: ")
        print(data.decode("utf-8"))

    elif entry == "4":
        name = input("Customer Name: ")
        s.send(bytes(name, "utf-8"))
        age = input("New Customer Age: ")
        s.send(bytes(age, "utf-8"))
        data = s.recv(9999)
        print("Server response: ")
        print(data.decode("utf-8"))

    elif entry == "5":
        name = input("Customer Name: ")
        s.send(bytes(name, "utf-8"))
        addr = input("New Customer Address: ")
        s.send(bytes(addr, "utf-8"))
        data = s.recv(9999)
        print("Server response: ")
        print(data.decode("utf-8"))

    elif entry == "6":
        name = input("Customer Name: ")
        s.send(bytes(name, "utf-8"))
        num = input("New Customer Number: ")
        s.send(bytes(num, "utf-8"))
        data = s.recv(9999)
        print("Server response: ")
        print(data.decode("utf-8"))


    elif entry == "7":
        data = s.recv(9999)
        print("Server response: ")
        print(data.decode("utf-8"))

    elif entry == "8":
        running = False
        print("Thank you for using this program!")

    else:
        print("Wrong input, please enter a valid one.")


