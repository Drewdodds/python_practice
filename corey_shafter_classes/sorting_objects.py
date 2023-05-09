# In this file we will look at how to sort diferent python data types as well as objects. 
# to get started let's look at how to sort a list. 

li = [9,1,8,2,7,3,6,4,5] # here is a list that contains a bunch of numbers between 1 and 9. What if we wanted to sort this?

s_li = sorted(li) # new var and we passed the original list as the object to sort. 

print('Sorted Variable:\t', s_li) # this sorts it.

#what if you wanted to sort it without creating a new var? Instead of using the sorted() function you can use the sort() method. 

# li.sort()
# print(li) # this does the same thing. 

# the diff between the sort function vs the method is that the function actually returns a new list. So the method actually returns "none"
# if you did s_li = li.sort() it would return None. 

# How can we sort in decending order?

s_d_li = sorted(li, reverse=True)
print(s_d_li) # this is in decending order

# and you can use the same parameter in the method
li.sort(reverse=True)

# why would I want to choose the sort function over the method? Well that sort method on the list is fine if you are working with lists and if you want to 
# modify it in place but the sorted functions gives us more flexibitlity b/c we can pass in any iterable as opposed to the sort() method
# which works specifically on lists.
# Example on a tuple

tup = (9,1,8,2,7,3,6,4,5) # the tuple does not have a sort method. You would get an error with sort() so you have to use the function. 

s_tup = sorted(tup)
print(s_tup) # now you can see that our tup value is a sorted list.

# Another example with a dict. 

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'} # you can pass a dict into the sorted function
s_di = sorted(di)
print(s_di) # this will sort the keys and you can see that it returns the keys sorted in alphabetical order

# so far we have sorted integers in asc and desc order. What if we wanted to sort values based on a different criteria?

# ex: what if we wanted to sort the list below based on their absolute value?
li_2 = [-6,-5,-4,1,2,3]
s_li_2 = sorted(li_2, key=abs) # sort based on absolute value
print(s_li_2)

# the key parameter is extremely useful when you're sorting objects with named attributes so for ex see the class object below

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        def __repr__(self):
            return '({},{},${})'.format(self.name, self.age, self.salary)

# sampel employees
e1 = Employee('Carl', 37, 700000)
e2 = Employee('Sarah', 29, 800000)
e3 = Employee('John', 43, 900000)

# put the employees in a list
employees = [e1, e2, e3]

# sort them based on a attribute

s_employees = sorted(employees)

