# Create function

# def say_hello(name):
#     print(f'Hello {name}')

# say_hello('Robin Winters') # output: Hello Robin Winters

# Function with default parametr

# def say_hello_default_arg(name = 'Sam'):
#     print(f'Hello {name}')

# say_hello_default_arg() # output Hello Sam

def get_sum(num1, num2):
    total = num1 + num2
    return total

result = get_sum(5, 15)
print(result) # output 20