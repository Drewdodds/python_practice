# Here we b elearning how to create and use classes within python and how object oriented concepts are applied within python. 
# There is a lot to cover so this small series is broken into different parts of the concept. 
# We'll cover the basics of creating and initiationg classes. We'll learn bout inheritance class and instance variables. 
# Static methods and class methods as well as several other topics. 

# In this vid we'll cover creating and initiatiing simple classes. 

# Why should we use classes? It's used in a lot of programming langauges you will notice. 
# They allow us to logically group our data and functions in a way that's easy to reuse and also easy to build upon if need be. 

# Side note: When we say "data and functions that are associated with a specific class"...We call those attributes and methods.
# When we say "method" we mean a function that is associated with class. 

# Hypothetical scenario we will work with and build upon. Say we had an application for our company and we wanted to represent our employees in our code. 
# This is agreat use case for a class b/c each individual employee is going to have specific attributes and methods. 
# Ex: Each employee is going to have a name, email address, pay, etc. It would be nice if we just had a class that we could use as a blue print to create an employee.
# So that we did not have to do that manually each time from scratch. 

# Let's create a simple employee class. 
# There is a diff between a class and an intance of a class
# So our class is a blueprint for creating instances and each unique employee that we create using the blue print will be an instance of that class.
# We'll get deeper into instance varaiables and class variables. In this vid we will talk about instance vars. Instance variables contain data that is
# unique to each intance. 
# So to avoid having to set up unique vars per employee manually we use a special init method.

class Employee: 
    
    def __init__(self, first, last, pay): # these are instances within the class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
    def fullname(self): # each method within a class automatically takes the instance as the first argument and we're going to always call that "self".
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Drew','Dodds',50000)
emp_2 = Employee('Corey','Schafer',60000) # So everything we have so far (like name, etc) are all attributes of our class now. 
# now let's say we wanted the ability to perform some kind of action...now to do that we can add some methods to our class.
# What if we wanted the ability to display the full name of an employee now. See above code beneath email attribute. 

print(emp_1.first)

print(emp_1.fullname()) # here we call our custom method we created within the employee class. We need the parenthesis here b/c it's a method. 