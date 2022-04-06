name = 'Robin'
age = 34

# Concatenate

# print('Hello, my name is ' + name + 'and I am ' + str(age) + 'years old...')

# String Formatting

# Arguments by position

# print('My name is {name} and I am {age} years old...'.format(name = name, age = age))

# F-Strings (3.6+ versions)

# print(f'My name is {name} and I am {age} years old...')


s = 'Hello, World!'
# Capitalize String
# print(s.capitalize())

# Make all Uppercase
# print(s.upper())

# Make all lower
# print(s.lower())

# Swap case
# print(s.swapcase())

# Get length
# print(len(s))

# Replace
# print(s.replace('World', 'everyone')) # output 'Hello, everyone!

# Count
# sub = 'h'
# print(s.count(sub)) # output 0 -case sensetive-
# print(s.count('H')) # output 1

# Starts with
# print(s.startswith('hello')) # output false - case sensetive -
# print(s.startswith('Hello')) # output true

# Ends with
# print(s.endswith('!')) # output true

# Split into a list
# print(s.split()) # output ['Hello,', 'World!']

# Find the Position
# print(s.find('r')) # output 9

# Is all alphanumeric
# print(s.isalnum()) # output false

# Is all alphabetic
# print(s.isalpha()) # output false -empty space and , and ! - 

# s1 = 'HelloWorld'
# print(s1.isalpha()) # output true

# Is all numeric
# print(s.isnumeric()) # output false