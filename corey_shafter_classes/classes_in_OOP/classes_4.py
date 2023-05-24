# In this video we will be learning about class inheritance. Inheritance allows us to inherit attributes and methods from a parent class.
# So we can create sub-classes with their own attributes and then also be able to access the parent attributes and methods b/c they are inherited. 
# We can also override the inherited data on the sub class if we want and it not affect the parent class. 
# Let's look at a real world example. Going back to the employee class we have been working with.
# What if we wanted to create different types of employees? Say, let's make developers and managers.
# so these new sub classes we will make will need to hav first and last name, email, etc. But we already have that in the employee parent class. So it can use that. 

class Employee: 
    raise_amount = 1.04

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'


    def fullname(self): 
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

# creating sub class here:
class Developer(Employee): # this will now inherit the attributes from the employee class
    raise_amount = 1.10 # custom raise that's on the child level
    
    def __init__(self, first, last, pay, prog_lang): # so here, the this new init method will pass in the parent attributes, and then dev will pass in prog lang.
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee): # new sub class
    
    def __init__(self, first, last, pay, employees=None): # the employees attribute being a list of emps they manage. So we will pass that list in.
      super().__init__(first, last, pay)
      if employees is None:
          self.employees = []
      else:
          self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employees.append(emp)

    def remove_emp(self, emp):
            if emp in self.employee:
                self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())



dev_1 = Developer('Drew','Dodds',50000, 'Java')
dev_2 = Developer('Corey','Schafer',60000, 'Rust')
# so what if you wanted to pass in the employee level attributes like on the two above plus a new one on the child level? Let's pass a programming lang as an attribute
# to get around this, you will have to give the developer class it's own init method.
dev_3 = Developer('Jon' , 'Doe', 70000, 'Python')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.print_emps()

#print(dev_3.prog_lang)


# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)