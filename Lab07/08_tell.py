filename = "sample01.txt"

with open(filename, "r") as file:
    print(f"Tell before reading: {file.tell()}")
    file.read(7)
    print(f"Tell before reading: {file.tell()}")
    file.read()
    print(f"Tell before reading: {file.tell()}")
