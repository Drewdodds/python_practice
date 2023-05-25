# Functions are basiaclly some instructions packaged together that perform a specific task.
# So let's create our first function and see why these are so beneficial. 
# Classic function: we'll use the def keyword
# functions allow s to reuse our code with out repeating yourself. 
# you can't leave a function blank so if you happen to not be ready to use it you can just enter "pass" below in the indented code block portion of the function
#(within the scope of the function)
#def hello_function():
#    pass

def hello_function():
    pass

print(hello_function) # output = <function hello_function at 0x00000204BDD3D1F0> b/c we didn't actually run it. We need to also call the parenthesis like below

print(hello_function()) # prints none bc I have "pass"

# let's do an actual workable function. 

def func():
    print('Hello Function!')

func()

# some more comments about functions. What if you had a big application that called for the hello function output many times? And all the sudden, 
# the boss wanted the output to have a period instead of a exclamation mark? Well, you don't have to edit the print call 1000s of times. Just the function itself. 
# This is called DRY coding. Which stands for "don't repeat yourself".
# It's a command mistake for new programmers to constantly repeat and write the same code when really they can put that code in variables and functions so that it's in a single location.

# What does it mean to "return" somthing? This is were functions can become powerful. Funntions allow us to operate on some data and then pass
# the result to the call of our function.See exampl below.

def ex_return():
    return 'Hello return example' # what does this mean exactly? This means that when we execture our function it's actually going to be eqwual to our return value.

# So if I execute the function (like below) it equals the string within the code block.

print(ex_return())

# so think of a function as a machine that takes in a input and produces a result. For more fancy function, you can think of it as a black box. (It can be helpful but when 1st started don't get hung up on it)
# You don't really need to think through how exactly it does what it does. You are more concerned about the input and return value.

# example of one with a required argument variable
def ex_three(greeting):
    return '{} Function.'.format(greeting)

print(ex_three('Hi'))

# example of one with two parameter variables with a default value
def ex_four(greeting, name = 'You'):
    return '{}, {}.'.format(greeting,name)

print(ex_four('Hi', 'Drew'))
# or
print(ex_four('Hi', name = 'Drew'))

# Another method. What the following mehtod allows is for the function to accept an arbitrary number of positional or keyword inputs.

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)

# Another way where we pass a list object as the 1st parameter and a dict as the 2nd.
def student_info_two(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math','Art']
info = {'name': 'John', 'age': 22}

print(student_info(*courses, **info)) #we do the * syntax b/c it will unpack each value individually
