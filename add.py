def add(name, age, addr, num):

    f = open("data.txt")
    lines = f.readlines()

    data = ""

    for line in lines:
        if name in line:
            data = line

    f.close()

    if data == "":

        data = name + "|" + age + "|" + addr + "|" + num

        f = open("data.txt", "w")

        for line in lines:
            if line != '\n':
                f.write(line)
        f.write(data + "\n")
        f.close()
        return "The customer has been added!"

    else:
        return "The customer is already in the database."








