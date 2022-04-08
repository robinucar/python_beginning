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


