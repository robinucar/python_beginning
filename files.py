# Python has functions for creating, reading, updating, and deleting files.

# Open a file

myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name) # output:  Name:  myfile.txt
print('Is Closed: ', myFile.closed) # output: Is Closed:  False
print('Opening Mode: ', myFile.mode) # output: Opening Mode:  w