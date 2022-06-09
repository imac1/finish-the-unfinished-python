# Implement flowchart "Prime" here.

# Give me an integer (greater than 1)
# Possible outcomes:
# - Not an integer
# - Too small
# - Not prime
# - Prime

number = int(input("Give me a number greater than 1 \n"))
i = 2
while i < number:
    if not isinstance(number, int):
        print("not an integer")
    elif number < 2:
        print("too small")
    
    if number % i == 0:
        print("Not prime")
        break
    else: 
        i = i + 1
else: 
    print("prime")




