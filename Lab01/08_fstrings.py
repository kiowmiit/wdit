sample_fstring = f"Sample f-string"
print(sample_fstring)

quantity = 67.64736278423

formatted_fstring = f"The quantity is {quantity}"
print(formatted_fstring)

fstring_with_limited_accuracy = f"The quantity is {quantity:,.2f}"
print(fstring_with_limited_accuracy)

price = 10
tax = 0.2

fstring_with_expression = f"The price after tax is: {price + price * tax}"
print(fstring_with_expression)

old_format = "The price after tax old way is: {}".format(price + price * tax)
print(old_format)
