# In the first vid we went over instance varaibles. Now we will go over class variables
# Class variables are variables that are shared across all instances of a class. It's a higher level variable that applies to all instances within the same class
# So while instance variables can be unique for each instance like our names and email and pay...
# Class varaibles should be the same for each instance. So looking at our employee class below...what kind of data do we want to be shared across all employees?
# For this example we will say that this will be a standard raise that all empployees will get.
# To do this you will add the class variable to the top of the code block. See the two added below before the initiation of the emp instances.


class Employee: 
    raise_amount = 1.04 # Here is the class variable
    num_of_emps = 0 # another class var that we will increment it by 1 each time we create a new employee.

    def __init__(self, first, last, pay): # these are instances within the class. The self attribute is always automatic and first. The attributes after can be whatever you want to create.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

        Employee.num_of_emps += 1 # this will increment the class var by 1 each time we make an employee

    def fullname(self): # Here, we defined a method for this class. Each method within a class automatically takes the instance as the first argument and we're going to always call that "self".
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) # you have to access it either by accessing the class var or instance var 'self'.

emp_1 = Employee('Drew','Dodds',50000)
emp_2 = Employee('Corey','Schafer',60000)

emp_1.apply_raise()
print(emp_1.pay)
