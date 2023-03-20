# A Dictionary is a collection which is unordered, changable and indexed. No duplicate members.

# Create a dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

print(person, type(person))

# Get Value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value

person['phone'] = '555-555-5555'

print(person)

#get dict kys

print(person.keys())

#get items
print(person.items())

# copy dict

person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# remove an item from a dict
del(person['age'])
#person.pop('phone') -- another way to delete key/value pair

print(person)

# list of dicts (an arrary of dicts)

people = [
    {'name': 'Martha', 'age':30},
    {'name': 'Kevin','age': 25}
] 

print(people)

# getting values from a list of dicts
print(people[1]['name'])