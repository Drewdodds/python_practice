# In the last vid we learned about the diff between instance variables and class variables. 
# in this vid, we'll be learning about the diff between regular methods, class methods, and static methods. 
# As we learned in the 1st vid... regular methods in a class automatically take the 1st instance var as the 1st argument.. based on condition we were calling this "self". 
# How can we change this so that it auto takes the class as the first argument?
# To do that, we are going to use class methods. We are going to add a "decorator" under the defined methods below. "@classmethod"0
# Adding this decorator will alter the method so that it takes in the class first instead of the first instance within the class.
# The common namming convention for the class method is "cls". 
# So there are intance variables as well as class variables. There are also instance methods as well as class methods. 
# here we have the class varible called raise_amount where the value is 1.04. 
# However, we can create a class method that modifies that and sets a new value to it. 
# Lastly, what is a staic method? They are methods that don't pass anything as the first instance automatically. So really, they act like normal functions. 
# BUT they do logically connect to a class somehow so you wnat to include them. See example below. Let's say we wnated a simple function that would take in
# a date and return whether or not it was a work date. So that has a logical connection to the employee class but it does not actually depend on any
# specific instance or class variable so we are going to make it a static method.


class Employee: 
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

        Employee.num_of_emps += 1 

    def fullname(self): # instance method
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self): # instance method
        self.pay = int(self.pay * Employee.raise_amount) 
    
    @classmethod # Class method
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @staticmethod # Class method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 

emp_1 = Employee('Drew','Dodds',50000)
emp_2 = Employee('Corey','Schafer',60000)

emp_1.apply_raise()
print(emp_1.pay)
