num1 = int(input('Enter your your first number: '))
num2 = int(input('Enter your second number: '))
op = input('Enter an operator: ')

if op == '+':
    print(f'{num1} + {num2} = ', num1+num2)
elif op == '-':
    print(f'{num1} - {num2} = ', num1-num2)
elif op == '*':
    print(f'{num1} * {num2} = ', num1*num2)
elif op == '/':
    print(f'{num1} / {num2} = ', num1/num2)
elif op == '%':
    print(f'{num1} % {num2} = ', num1%num2)
else:
    print('Invald operator')