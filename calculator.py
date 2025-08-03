# user chooses two numbers(use input function)
# convert the two numbers into floating point numbers
# choose an arithmetic operation between the following options : +,-,*,/
number_1 = int(input('Enter the first number : '))
number_2 = int(input('Enter the second number : '))
op = input('Enter an arithmetic operations among the following options (+,-,*,/):')
if op == '+':
    result = number_1+number_2
    print(f"{number_1} + {number_2} = {result}")
elif op == '-':
    result = number_1-number_2
    print(f"{number_1} - {number_2} = {result}")
elif op == '*':
    result = number_1*number_2
    print(f"{number_1} * {number_2} = {result}")

elif op == '/':
    if number_2 != 0:
        result = number_1 / number_2
        print(f"{number_1} / {number_2} = {result}")

    elif number_2 == 0:
        print('Division by zero does not exist')
