# do something or evauate each value in a object (usually with multiple values)
# for loops
nums = [1,2,3,4,5]

for num in nums:
    print(num)

# Importnat key words: "Break" (will complately break out of loop) and "Continue" (will move on to the next iteration of the loop)

# Break example. Let's say we are looking for a specific number in our list and once we find it we don't need to continue. 

for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)
# this loop broke once we reached 3

# What if we wanted to ingnore the value but not break out of a loop completely
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)
    # this one prints found for 3 and then continues.

#loop within a loop:

for num in nums:
    for letter in 'abc':
        print(num, letter)

# there will be times when we just want to go through a loop a certian number of times. There is a built in function called range that is useful for this.
# Let's say we wanted to run through a loop 10 times

for i in range(10):
    print(i)

# While loops
x = 0

while x < 10:
    print(x)
    x += 1
# After printing the value of x, this line increments the value of x by 1. The += operator is shorthand for adding a value to a variable. So, x += 1 is equivalent to x = x + 1. 
# you can also break out of the while loop
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

