filename = "sample01.txt"

with open(filename, "w") as file:
    file.write("Hello World")
    file.write("Same line\n")
    file.write("This is new line")
