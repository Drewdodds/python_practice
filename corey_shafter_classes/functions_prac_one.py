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

