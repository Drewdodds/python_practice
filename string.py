# strings in python are surrounded by either single or double quotes. Let's look at string formatting and some string methods
name = 'Brad'
age = 37

#Concat
print('Hello, my name is '+ name + 'and I am ' + str(age))

#String formatting

#positional arguments
print('My name is {name} and I am {age}'.format(name=name, age=age))#if you use this way you have to use format to confomr the data types. Below is better

#F-Strings 
print(f'Hello, my name is {name} and I am {age}')

#string methods
s = 'hello world'

#captilize string
print(s.capitalize())