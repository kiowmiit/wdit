
age = int(input("Enter your age:"))
print(f"your age is {age}")

try:
    float_number = float(input("Enter your float number:"))
    print(f"your float number is {float_number}")
except ValueError:
    print("You didn't enter a number.")