# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in python is an object

# Create a class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
 # you can add a method(s) to the class   
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

# Init or initialize user object
drew = User('Drew Dodds','dodd@gmail.com','31')

print(type(drew)) # and you can see that it's a user

# access properties
print(drew.name)

print(drew.greeting())
