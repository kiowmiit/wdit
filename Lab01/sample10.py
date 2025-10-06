name = input("Please enter your name: ")
print(f"Hello: {name}. Nice to meet you.")

number_integer = int(input("Please enter integer number: "))
print(f"The integer number is {number_integer}")

number_float = float(input("Please enter float number: "))
print(f"The float number is {number_float}")

number_to_cast = input("Please enter a number (float or decimal): ")
number_casted = 0

#użycie instrukcji try w celu wyłapania błedu rzutowania
try:
    number_casted = int(number_to_cast)
except ValueError:
    print("Cannot cast a float string into integer")

print(number_casted)
