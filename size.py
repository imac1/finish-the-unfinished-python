# Implement flowchart "Size" here.

# Give me your size:

# Based on the input, display
# - Oh, this is small.
# - This size is medium.
# - Huh, this is large.
size = int(input('Please, give me your size \n'))
if size <= 10:
    print('Oh, this is small!')
elif size <= 80:
    print('This size is medium')
else:
    print('Huh, this is large')