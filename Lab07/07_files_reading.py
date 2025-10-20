filename = "sample01.txt"

# reading character by character
with open(filename, "r") as file:
    four_chars = file.read(4)
    print(four_chars)
    more_chars = file.read(25)
    print(more_chars)
    rest_of_chars = file.read()
    print(rest_of_chars)

# reading line by line
with open(filename, "r") as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()

# reading all lines at once
with open(filename, "r") as file:
    lines = file.readlines()
    print(lines)