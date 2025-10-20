integer_number = 1
second = 2
float_number = 3.14
integer_string = "415"
float_string = "3.14"
invalid_string = "Hello world!"

print("Cast float to integer: " + str(int(float_number)))
print("Cast string to integer: " + str(int(integer_string)))

print("Cast integer to float: " + str(float(integer_number)))
print("Cast string to float: " + str(float(float_string)))

print("Cast integer to string: " + str(integer_number))
print("Cast integer to string: " + str(float_number))

print("Cast invalid string to float: " + str(float(invalid_string)))

