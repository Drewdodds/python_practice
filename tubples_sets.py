# A tuple is a collection which is orderd and unchangable. Allows duplciate members.

#Create a Tuple
fruits = ('Apples','Oranges','Grapes')
print(fruits)
print(type(fruits))

#get a value from a tuple
print(fruits[1])


# delete tuple (or anythng)
#del fruits

# A Set is a collection which is orderd and unindexed. No duplciate members. 

# Create a Set
fruits_set = {'Apples', 'Oranges', 'Mango'}

print(fruits_set)

#check in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

#remove from set
fruits_set.remove('Grapes')
print(fruits_set)


#clear set

fruits_set.clear()
print(fruits_set)
