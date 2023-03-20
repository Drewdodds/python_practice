# Python has functions for creating, reading, updating, and deleting files.

# open a file

myfile = open('myfile.txt', 'w')

# get info on this files

print('Name: ', myfile.name)
print('Is Closed: ', myfile.close)
print('Opening Mode: ', myfile.mode)

# Write to file

myfile.write('I love Python')
myfile.write(' and JS')
myfile.close()

# append to file

myfile = open('myfile.txt', 'a')
myfile.write(' I also like PHP')
myfile.close()

# read from a file 
myfile = open('myfile.txt', 'r+')
text = myfile.read(100)
print(text)