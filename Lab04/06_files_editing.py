filename = "sample01.txt"

with open(filename, "r+") as file:
    for line in file:
        print(line)
    file.write("\nNew line at the end")
    