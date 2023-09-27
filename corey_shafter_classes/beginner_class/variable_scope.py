# In this vid we will learn about Variable scope in python. This is an important concept. 
# B/c it's something that you will need to understand in almost every program  you write. 
# Understanding this may help with a var may not have the value we expected and we need to debug our code. 

# Variable scope determines where our variables can be accessed from within the program and what values those variables hold in different contexts.

# There is a common abbreviation for understanding the scoping rules within Python and that abbreviation is "LEGB"
# Which stands for Local, Enclosing, Global, Built-in.

# Local are vars defines within a function.
# Enclosing are vars in the local scope of enclosing functions
# Global are vars defined at the top level of the module or explxitly declared global using the global keyword
# Built-ins are just names that are preassigned in Python

# They are listed in this order b/c this is the order in which Python checks to see where they are applied. Global and local are the most common.

# Global and local
x = 'global x' # The var x here is a global var b/c it is in the main body of our file

#now we make a function
# def test():
#     y = 'local y' # this is a local var to this test function.
#     print(y) # comment this out for test below.
#     print(x)

# print(y) # this prints out the local y. Python uses the LEGB rule when I print out the y var. y is local (first in priority) so it prints it out.

# if we comment out the print y function and add print(x) then it will print x. It checks for local x and there isn't one. It then checks for enclosing and ther isn't one. 
# it finnaly check global and there is one. So it prints that. 

# let's try something else with the following code bloack. 

# def test():
#     x = 'local x' # this is a local var to this test function.
#     #print(y) # comment this out for test below.
#     print(x)

# test()
# print(x) # so if you run this you can see it printed the local x to the function and then the global x which is differently defined. 
# The global x var does not over write the local b/c it is defined differently.

# What is we did want to set a new value for the global x var WITHIN the scope of the function? We have to tell python to do that.
# To do that we add that to the scope of the function as seen re-written below
# def test():
#     global x
#     x = 'local x' # this is a local var to this test function.
#     #print(y) # comment this out for test below.
#     print(x)

# test()
# print(x) # this then prints out the global one both times b/c we told python to do so.

# Sometimnes it can be tempting to learn something new and then overuse it. I wanted to show you the global statement so that you know what it does and how to use it. 
# but I don't think I've ever had the need to use this myself and if you find yourself using it often then you are probably doing something wrong. 
# Using the local scope of a function make it easier to understand and easier to work with. So you can imagine how difficult it would be to maintain our coude
# if you use the global statments and had to worry about vars and your functiosn overriding values outside of that function.
# So with the local scope being self contained it allows us to not have to worry about what is going on outside of the function.

# Let's now look at the built in scope. It is just names that are preassigned in Python. Example - min() is a built in function that finds the smallest value of a iterable.
# Example:
# m = min([5,1,4,2,3])
# print(m) # we were able to use min() b/c it's a built in function. If we want to veiew the variables within this function we can...
# import builtins
# print(dir(builtins)) 
# one thing you want to be careful of as far as builtins is accidently overriding them. If you were to create a new function called min() you could overright what it is.

# now let's look at enclosing scrope. 

def outer():
    x = 'outer x' #local x to the outer function
    def inner():
        x = 'inner x' #local x to the inner function
        print(x)

    inner()
    print(x)

outer() # this prints out the print statement from both functions. BUT if you were to comment out the 'x = 'inner x'' then it would print out outer x twice. 
# b/c for that first inner() function it's checking local first. If there is not one is goes one step up and looks at anything enclosing - which there is one in the outer() function.

