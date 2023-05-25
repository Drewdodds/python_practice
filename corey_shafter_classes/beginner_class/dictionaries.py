# Dictionaries allow us to work with key value pairs. In other programming languages these can be cashed hash maps or accociated arrays.
# Key values pairs are where the key unique indentifier where you can find that data and the value is that data. 

student = {'name': 'John', 'age': 25,'courses': ['Math','CompSci']}
# full print
print(student)

#access the name key. It will print the value
print(student['name'])

#access the keys
print(student.keys())

#access the values
print(student.items())

#add a new entry to the dict
student['phone'] = '555-555-5555'

print(student)

# you can change a value as well using the same way
student['name'] = 'Jane'
print(student)

#You can also update values using the update method. This can be useful if you wanted to update multiplie values at a time.
student.update({'name': 'Drew', 'age': 27,'cell phone': '864-760-8028'}) #here we changed values and added the cell phone key value
print(student)

#remove an entry with del
#del student['age']
#print(student)

#delete with pop method which returns that value
age = student.pop('age')
print(age)

#looping through all the keys and values in the dict
# how many values are in teh dict?
print(len(student))
print(student.values())
print(student.items())
print(student.keys())

#looping
#printing keys
for key in student.items():
    print(key)

# printing key and value
for key, value in student.items():
    print(key, value)