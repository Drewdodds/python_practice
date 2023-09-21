# If/ Else conditions are used to decide to do something based on something being true or false
x = 10 
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

#If/Else
a = 10
b = 50
if a > b:
    print(f'{a} is greater than {b}')
else: 
    print(f'{b} is greater than {a}')

#elif | basically a case statment in SQL
c = 10
d = 10
if c > d:
    print(f'{c} is greater than {d}')
elif c == d: 
    print(f'{c} is equal {d}')
else: 
    print(f'{d} is greater than {c}')

# Nested if statement (if within an if)
e = 3
f = 10
if e >2:
    if e <= 10:
        print(f'{e} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) - Used to combine conditionals statements
if e > 2 and e <= 10:
    print(f'{e} is greater than 2 and less than or equal to 10')

if e > 2 or e <= 10:
    print(f'{e} is greater than 2 or less than or equal to 10')

#not
if not(e == f):
    print(f'{e} is not equal to {f}')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object. 
numbers = [1,2,3,4,5,6,7,8,9]
# in
i = 3
if i in numbers:
    print(i in numbers)
#not in
j = 11
if j not in numbers:
    print(j in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
k = 10
l = 10
if k is l:
    print(k is l)