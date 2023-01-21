def delete(name):

    f = open("data.txt", "r")
    lines = f.readlines()

    data = ""

    for line in lines:
        if name in line:
            data = line
    f.close()



    if data == "":
        return "The customer is not in the database."

    else:
        f = open("data.txt", "w")
        for line in lines:
            if line != data and line != "\n":
                f.write(line)
        f.close()
        return "The customer has been deleted!"