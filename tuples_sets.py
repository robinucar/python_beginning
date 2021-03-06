# TUPLE

# Create tuple

fruits = ('Apples', 'Oranges', 'Grapes')
# or using contructor

# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# # or

# fruits3 = "Javascript", "Python", "Ruby"

# print(fruits, fruits2)
# print(fruits, type(fruits))
# print(fruits3, type(fruits3))

# Single valu needs trailing comma :)
# fruit = ('Apples') # type return string
# fruit1 = ('Apples',) # type return tuple

# Get value by index

# print(fruits[1])

# Cannot change the value
# fruits[0] = 'Pears'
# print(fruits) # output: TypeError: 'tuple' object does not support item assignment

# Delete tupple

# del fruits
# print(fruits) # output : NameError: name 'fruits' is not defined - It was deleted -

# Get length

# print(len(fruits)) # output: 3


# SET

# Create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

# or using constructor

# fruits_set1 = set(('Apples', 'Oranges', 'Mango'))

# print(fruits_set, type(fruits_set))

# print(fruits_set1, type(fruits_set1))

# Check if an element is exist inside the set

# print('Apples' in fruits_set) # output: True

# Add an element to the set

# fruits_set.add('Grape')
# print('Grape' in fruits_set) # output: True

# Remove an element from the set
# fruits_set.remove('Apples')
# print(fruits_set) # output : {'Oranges', 'Mango'}

# Clear the set
# fruits_set.clear()
# print(fruits_set) # output: set() -Empty set-

# Delete set
# del(fruits_set)
# print(fruits_set) # output: NameError: name 'fruits_set' is not defined - It was deleted -

# Cannot add an element twice
# fruits_set.add('Apples')
# print(fruits_set) # output: {'Oranges', 'Apples', 'Mango'} - no error, but not adding an element twice -