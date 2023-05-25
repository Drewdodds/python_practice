# Numbers are most commonly represetned as either integers or floats. Int3eger is a whole number and a float is a decemial.
num = 3
num_2 = 2.3
#check type (type  = int, type float)
print(type(num))
print(type(num_2))

# you can also do common arithmetic operators
# addition:       3 + 2
# subtraction:    3 - 2
# Mutliplication: 3 * 2
# Division:       3 / 2
# Floor division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

print(3+2)
print(3**2)
# a good way to check if a number is even you can do the modular operator
# modulare operator gives us the remainder after a division so 3 % 2 will have a remainder of 1. B/c 2 goes into 3 once with 1 left over.
# Commion use case is if you do a mod 2 on any number and there  is no remainder then that number is even. If there is a remainder, then that number is odd
#print(3%2) #=1
#print(2%2) #=0 b/c 2 goes into 2 once with no remainder so it equals 0

# let's look at the order of operations. You can do this with parenthesis. 
print( 3 * 2 + 1) # = 7
print( 3 * (2 + 1)) # = 9

# incrementing a varaible
num_3 = 1 

# first way
num_3 = num_3 + 1 # and you can see it = 2 b/c it went up by 1.
print(num_3)
# more common way
num_4 = 1
num_4 += 1
print(num_4)

# comparison operators
# Equal:            3 ==2 
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3< 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num5 = 3
num6 = 2
print(num5 == num6)