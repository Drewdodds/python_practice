# A List is a collection which is ordered and changable. Allows duplicate members.

# Create list

numbers = [1,2,3,4,5,]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor 
numbers2 = list((1,2,3,4,5))

#Get a single value from a list

print(fruits[1])

#Get length

print(len(fruits))

# Append (to the end) of a list
fruits.append('Mangos')

print(fruits)

#remove from list
fruits.remove('Grapes')

print(fruits)

#Insert ito position
fruits.insert(2, 'Strawberries')
print(fruits)

#remove from certian poisitions
fruits.pop(2)
print(fruits)

#reverse list
fruits.reverse()
print(fruits)

#sort
fruits.sort()
print(fruits)

#reverse sort
fruits.sort(reverse=True)
print(fruits)

#Change a value
fruits[0]='Blueberries'
print(fruits)