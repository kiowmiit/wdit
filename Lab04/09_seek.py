filename = "sample01.txt"

with open(filename, "r+") as file:
    file.seek(2)
    file.write("e")
    file.seek(0)
    lines = file.readlines()
    print(lines)
    lines = file.readlines()
    print(lines)
    file.seek(file.tell()-1)
    print(f"Reading last character of file: {file.read(1)}")
