# Python has functions for creating, reading, updating, and deleting files.

# Open a file

myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name) # output:  Name:  myfile.txt
print('Is Closed: ', myFile.closed) # output: Is Closed:  False
print('Opening Mode: ', myFile.mode) # output: Opening Mode:  w

# Write to file
myFile.write('I Love Python. ')
myFile.write('I am learning Python.')

# Close file
myFile.close()
print('Is Closed: ', myFile.closed) # output: Is Closed:  True

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write(' I also would like to learn Django.')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100) # -100 is character number-
print(text)