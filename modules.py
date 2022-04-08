# A module is basically a file containing a set of functions to include in an application.
# There are core python modules, modules can be install using the pip package manager
# (including Django) as well as custom modules

# import a core module
import datetime

today = datetime.date.today()
print(today) # output: 2022-04-08

# or
from datetime import date
today = date.today()
print(today) # output: 2022-04-08

# Pip module
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello, i am robin')) # output: Hello, I Am Robin


