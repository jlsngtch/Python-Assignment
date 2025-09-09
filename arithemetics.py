num1 = float(input('Input the first num: '))
num2 = float(input('Input the second num: '))
operation = input('Enter your operaton (*, +, /, -): ')


if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

else:
    print("Invalid Operation")




