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
person['phone'] = '555-555-5555'
print(person.get('phone')) # output 555-555-5555
print(person) # output {'first_name': 'Robin Melsa', 'last_name': 'Winters', 'age': 34, 'phone': '555-555-5555'}