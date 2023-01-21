def find(name):

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
        return data