# In this vid we will learn how to use the property decorator. This allows us to give our class attributes getter setter and a leader functionality
# 

class Employee: 
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property # we aredefining our email in our class like it's a method but we're able to access it like it an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter # this will allow us to edit the full name of the instance using the the fullname method
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter # you can also set a deleter which will run that code when you use the del function with the class
    def fullname(self):
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email) # we aredefining our email in our class like it's a method but we're able to access it like it an attribute
print(emp_1.fullname()) # you can see here that we are not accessing fullname like an attribute and instead running it as is which is a method.