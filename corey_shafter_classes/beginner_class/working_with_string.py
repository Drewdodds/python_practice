# working with strings

message = 'Hello World'

print(message)

print(len(message))

# access characters individually. 
#access 1st character which would be "H"

print(message[0]) 

#access a range of charcaters
# the first index is inclusive. The second is not (0 is inclusive, 5 is not)
print(message[0:5]) 

# you can get the same thing by leaving off the first index (meaning it starts at the 1st)
print(message[:5]) 

# you can start at 6 for example and pull all the way to the end liks so

print(message[6:]) 

# Functions and methods are basically the same thing. A method is just a function that belongs to an object.
# string methods examples:

print(message.lower())
#count method
print(message.count('Hello'))
print(message.count('l'))

#find
print(message.find('World'))

# replace method
print(message.replace('World','Universe'))

#concatenating strings
greetting = 'Hello'
name = 'Drew'
# concating with +
new_message = greetting + ' ' + name
print(new_message)
#concating with f strings (place holders)
print(f'{greetting} {name}')