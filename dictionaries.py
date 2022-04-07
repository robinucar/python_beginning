# Create dict

person = {
    'first_name': 'Robin Melsa',
    'last_name': 'Winters',
    'age': 34
}


# print(person, type(person)) #output : {'first_name': 'Robin Melsa', 'last_name': 'Winters', 'age': 34} <class 'dict'>

# Or use a constructor to create a dict

# person2 = dict(first_name='James', last_name='Doe')

# print(person2, type(person2)) #output {'first_name': 'James', 'last_name': 'Doe'} <class 'dict'>

# Get Value

# print(person['first_name']) # output: Robin Melsa

# # Get value II Way

# print(person.get('last_name')) # output Winters

# Add key/value
# person['phone'] = '555-555-5555'
# print(person.get('phone')) # output 555-555-5555
# print(person) # output {'first_name': 'Robin Melsa', 'last_name': 'Winters', 'age': 34, 'phone': '555-555-5555'}

# Get dict keys
# print(person.keys()) # output dict_keys(['first_name', 'last_name', 'age'])

# Get dict items
# print(person.items()) # output dict_items([('first_name', 'Robin Melsa'), ('last_name', 'Winters'), ('age', 34)])

# Copy dict
# person2 = person.copy()
# print(person2) # output {'first_name': 'Robin Melsa', 'last_name': 'Winters', 'age': 34}

# person2['city'] = 'London'
# print(person2)
# print(person)

# Remove Item I way

# del(person['age'])
# print(person) # output {'first_name': 'Robin Melsa', 'last_name': 'Winters'}

# # Remove Item II way

# person.pop('last_name')
# print(person) # output {'first_name': 'Robin Melsa'}

# Clear dict
# person.clear()
# print(person) # output {} - Empty dict -

# Get the length
# print(len(person)) # output 3


# List of dict

people = [
   {'name': 'Robin', 'age': 34},
   {'name': 'Lisa', 'age': 31},
   {'name': 'Kathy', 'age': 32}
]

print(people) # output: [{'name': 'Robin', 'age': 34}, {'name': 'Lisa', 'age': 31}, {'name': 'Kathy', 'age': 32}]
print(people[0]) # output: {'name': 'Robin', 'age': 34}
print(people[1]) # output: {'name': 'Lisa', 'age': 31}
print(people[2]) # output: {'name': 'Kathy', 'age': 32}
print(people[0]['name']) # output Robin
# print(people[3]) # IndexError: list index out of range - First index is 0 -
