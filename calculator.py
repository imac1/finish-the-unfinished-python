# Implement flowchart "Calculator" here.

# First number
# Operation (+, -, *, /): ")
# Second number

# Possible outcomes:
# - Invalid input, try again
# - Division by zero is not allowed
# - or the result of the operation
n1 = 9
n1 = int(input('first number \n'))
while isinstance(n1, int):
    operator = input('operator')
    operators = ['+', '-', '/', '*']
    if operator in operators:
        n2 = int(input('second number \n'))
        if not isinstance(n2, int):
            print('invalid input, try again')
        if operator == '+':
            result = n1 + n2
            print(result)
            break
        elif operator == '-':
            result = n1 - n2
            print(result)
            break
        elif operator == '/':
            result = n1/n2
            print(result)
            break
        elif operator == '*':
            if n2 == 0:
                print('zero division not allowed')
                break
            else:
                result = n1*n2
                break
else:
    print("invalid input, try again")