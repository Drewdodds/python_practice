# Loops are used for iterating over a sequence (that is either a list, a tuple, a dict, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
    print(f'current person: {person}')

# Break out of the loop
for person in people:
    if person == 'Sara':
        break
    print(f'current person: {person}') # we just hit john and paul here

#continue in loop
for person in people:
    if person == 'Sara':
        continue
    print(f'current person: {person}') # Now we get John, Paul, and Susan. It didn't just stop the loop when it got to susan. It skipped over her.

# Range
for i in range(len(people)):
    print(people[i])

#custom range
for i in range(0,11):
    print(f'Number: {i}')

#While loops execute a set of statements as long as a condition is true.
count = 0 
while count <= 10:
    print(f'Count: {count}')
    count  += 1