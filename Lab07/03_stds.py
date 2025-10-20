import sys

# Dwa zapisy
print("Hello world!")
sys.stdout.write("Hello world!\n")

sys.stdout.write("Enter some string: ")
# funkcja flush użyta aby napis wyszedł na konsole
# przed pobraniem danych przez readline()
sys.stdout.flush()

# Dwa odczyty
user_input_stdin = sys.stdin.readline()
user_input_input = input("Enter some string:")

print(f"With sys.stdin {user_input_stdin} ")
print(f"With input {user_input_input} ")

try:
    print(float("D"))
except ValueError:
    print("Cannot cast to float", file=sys.stderr)