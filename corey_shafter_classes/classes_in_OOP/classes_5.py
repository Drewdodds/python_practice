# In this file we will learn about special (or Dunder) methods that we can use within our classes. 
# The special methods allow us to emulate some built-in behavior within Python. It;s also how we implement operator overloading.
# These special methods allow us to change built in behavior. These special methods are often surrounded by double under scroes. 
# __init__ is one of the most common ones. 
# Two other common ones are:
# __repr__ is meant to be an unambigous representation of the object and should be used for debugging and logging and things liek that. 
# It's really meant to be seen by other developers. 

# __str__ is meant to be a more readable representation of an object and is meant to be used as a display to the end user. 

class Employee: 
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay) # this will now print instead of the ambigous object name

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email) # this will now print instead of the ambigous object name

emp_1 = Employee('Drew','Dodds',50000)
emp_2 = Employee('Corey','Schafer',60000)
