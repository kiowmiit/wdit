import sys

name = input("Enter your name:")
age_string = input("Enter your age:")
age = None
try:
    age = int(age_string)
except ValueError:
    print("Cannot cast that data to age", file=sys.stderr)
    exit(86)

print(f"You are {name} and you are {age} years old")
