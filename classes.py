# Create a class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    # Define a method
    def greeting(self):
        return f'Hello, My name is {self.name} and I am {self.age} years old.'

    def has_birthday(self):
        self.age += 1

# Init user object
robin = User('Robin Winters', 'robinmelsaw@gmail.com', 34)
print(type(robin)) # output: <class '__main__.User'>
print(robin.name) # output:  Robin Winters
print(robin.greeting()) # output: Hello, My name is Robin Winters and I am 34 years old.

robin.has_birthday()
print(robin.age) # output : 35

# Extend Class

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'Hello, My name is {self.name} and I am {self.age} years old. And my balance is {self.balance}.'

# Init Customer

janet = Customer('Janet Jonson', 'janet@janet.com', 37)
janet.set_balance(500)
print(janet.greeting()) # output: Hello, My name is Janet Jonson and I am 37 years old. And my balance is 500.
