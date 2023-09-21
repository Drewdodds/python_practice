# A vriable is a container for a vaqlue, which can be of various types

'''
This is multiine comment or docstring (used to define a functuions purpose) an can be single or double quotes
'''

"""
Variable Rules:
- variable names are case sensitive (name and NAME are different variables)
- Must start with a letter or underscrore
- Can have numnbers but can not start with on 
"""

# the = sign assignes values
# x = 1           # int
# y = 2.5         # float
# name = 'John'   #str
# is_Cool = True  #bool

# Mutliple assignment
x, y, name, is_cool = (1,2.5, 'John', True) # this does exactly what we did above but all at once. 

#basic math
a = x + y

print(a)

#check type
print(type(x))

#casting a different type to a value
x = str(x)
y = int(y)
print(type(x))
print(type(y))
