from operator import not_


x = 10
y = 5
z = 50

# Simple if
# if x > y:
#     print(f'{x} is greater than {y}') # output : 10 is greater than 5

# If / else

# if x > z:
#     print(f'{x} is greater than {z}')
# else:
#     print(f'{z} is greater than {y}') # output: 50 is greater than 5


# if / elif / else
# if x > z:
#     print(f'{x} is greater than {z}')
# elif x < z:
#     print(f'{z} is greater than {y}')  # output: 50 is greater than 5
# else:
#     print(f'{x} is equal to {z}')


# Nested if

# if x > 2:
#     if x <= 10:
#         print('x is greater than 2 or less than or equal to 10') # output : x is greater than 2 or less than or equal to 10


# Logical Operators (and, or, not) - Used to combine conditional statements

# and
# if x > 2 and x <= 10:
#     print('x is greater than 2 and less than or equal to 10') # output : x is greater than 2 and less than or equal to 10

# or
# if x > 2 or x <= 10:
#     print('x is greater than 2 or less than or equal to 10') # output : x is greater than 2 or less than or equal to 10

# not
# if not(x == y): # output : 10 is not equal 5
#     print(f'{x} is not equal {y}')


# Membership Operators (not, not in) - Membership operators are used to test if a 
# sequence is presented in an object

numbers = [1,2,3,4,5,6,7,8,9,10]

# in
if x in numbers:
    print(x in numbers)

# in
if y in numbers:
    print(y in numbers)

# not in
if z not in numbers:
    print(z not in numbers)

