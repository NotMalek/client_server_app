import socket
from find import *
from update import *

while True:

    try:
        clientsocket.send(bytes("\nWelcome!", "utf-8"))

        entry = clientsocket.recv(9999).decode("utf-8")

        if entry == "1":
            name = clientsocket.recv(9999).decode("utf-8")
            data = str(find(name))
            clientsocket.send(bytes(data, "utf-8"))

        elif entry == "2":
            name = clientsocket.recv(9999).decode("utf-8")
            age = clientsocket.recv(9999).decode("utf-8")
            addr = clientsocket.recv(9999).decode("utf-8")
            num = clientsocket.recv(9999).decode("utf-8")
            data = str(add(name, age, addr, num))
            clientsocket.send(bytes(data, "utf-8"))

        elif entry == "3":
            name = clientsocket.recv(9999).decode("utf-8")
            data = str(delete(name))
            clientsocket.send(bytes(data, "utf-8"))

        elif entry == "4":
            name = clientsocket.recv(9999).decode("utf-8")
            change = clientsocket.recv(9999).decode("utf-8")
            data = str(update(name, "age", change))
            clientsocket.send(bytes(data, "utf-8"))

        elif entry == "5":
            name = clientsocket.recv(9999).decode("utf-8")
            change = clientsocket.recv(9999).decode("utf-8")
            data = str(update(name, "addr", change))
            clientsocket.send(bytes(data, "utf-8"))

        elif entry == "6":
            name = clientsocket.recv(9999).decode("utf-8")
            change = clientsocket.recv(9999).decode("utf-8")
            data = str(update(name, "num", change))
            clientsocket.send(bytes(data, "utf-8"))

        elif entry == "7":
            f = open("data.txt", 'r')
            content = f.read()
            clientsocket.send(bytes(content, "utf-8"))

    except:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", 9999))
        s.listen(5)
        clientsocket, address = s.accept()
        print(f"Connection has been established.")





