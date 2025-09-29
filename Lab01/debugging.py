def divide(a, b):
    return a / b

dividend = 10
divider = 5

result = divide(dividend, divider)

if result < 1:
    print('Dividend is larger than divider')
elif result == 1:
    print('Dividend and divider are equal')
else:
    print('Dividend is smaller than divider')
    
print('End of program')
