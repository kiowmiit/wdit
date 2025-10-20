invalid_float_string = "Hello world!"

try:
    float(invalid_float_string)
except ValueError:
    print("WARNING: value error")
else:
    print("No error")
finally:
    print("Executed after try block")

# try:
#     float(invalid_float_string)
# except (ValueError, TypeError) as e:
#     if(type(e) == ValueError):
#         print("WARNING: value error")
#     else:
#         print("Warning: type error")
# else:
#     print("No error")
# finally:
#     print("Executed after try block")


