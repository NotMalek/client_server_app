from delete import *
from add import *

def update(name, type, change):

    f = open("data.txt")
    lines = f.readlines()

    data = ""

    for line in lines:
        if name in line:
            data = line

    f.close()

    if data == "":
        return "The customer is not in the database."

    else:
        dataList = data.split("|")
        if type == "age":
            delete(name)
            add(name, change, dataList[2], dataList[3])
        elif type == "addr":
            delete(name)
            add(name, dataList[1], change, dataList[3])
        elif type == "num":
            delete(name)
            add(name, dataList[1], dataList[2], change)
        return "The customer's info were updated."

