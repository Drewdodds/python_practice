# A Function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces. 

# Create a function
def sayHello(name):
    print(f'Hello {name}')

sayHello('John Doe')

#establishing a default value
def sayHello(name = 'Sam'):
    print(f'Hello {name}')

sayHello()

# Usually you are going to deal with return values
def getSum(num1, num2):
    total =num1 + num2
    return total

print(getSum(3,4))

def getSum(num1, num2):
    total =num1 + num2
    return total

num = getSum(3,4) # here I just created a variable that has the function call with the numbers. I then printed the var below. 
print(num)


# A lambda function is a small anonymous function. It is "undefined"
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum2 = lambda num1, num2 : num1 + num2

print(getSum2(10,3))