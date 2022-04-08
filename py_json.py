# Json is commonly used with data APIS. Here how we can parse JSON into a Python dictionary.
import json

# Sample Json

userJSON = '{"first_name": "Robin", "last_name": "Winters", "age": 30}'

# Parse to dict
user_dict = json.loads(userJSON)
print(user_dict) # output: {'first_name': 'Robin', 'last_name': 'Winters', 'age': 30}
print(type(user_dict)) # output: <class 'dict'>
print(user_dict['first_name']) # output: Robin


# Covert dictionary to JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON) # output: {"make": "Ford", "model": "Mustang", "year": 1970}
