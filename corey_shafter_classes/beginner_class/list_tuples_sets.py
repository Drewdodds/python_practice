# lsit and tuples allow us to work with sequential data and sets are unordered collections of vbalues with no duplicates.
# Let's look at lists first

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses)) # shows us that we have 4 values in our list

# indexing to access values in Lists
print(courses[0])

# getting a range of values - this is called slicing
print(courses[0:2])

# negative indexing
print(courses[-1])

# Lists methods that allow us to modify our lists
courses.append('Art')
print(courses)

courses.insert(0, 'English')
print(courses)

# if you have multiple values you want to add you can use the extend method
new_courses = ['PE', 'Pychology']
courses.extend(new_courses)
print(courses)

#removing values from list
courses.remove('Math')
print(courses)

# pop will remove that last value by default
courses.pop()
print(courses)

#sorting list
#reverse list
courses.reverse()
courses.sort()

nums = [1,5,4,3]
print(nums)
nums_sort = sorted(nums)
print(nums_sort)

#other usful functions (min, max, sum)

print(min(nums))
print(max(nums))
print(sum(nums))

# finding values. If we wanted to find the certian index of a certian value then we can use the index method. 
print(courses.index('CompSci'))

print(nums.index(4))

print(3 in nums)

#for loop
for item in courses:
    print(item)

# it might be help to access the index and the value
for index, course in enumerate(courses):
    print(index, course)


# It's pretty common that we'll want to turn our list into strings separated by a value. We use a string method called join and pass the list throught it.
course_str = ' , '.join(courses)
print(course_str)

# We can also do the reverse of this and turn a string value back into a list type using the split method
new_list = course_str.split(',')
print(new_list)

# Tuples. These are similar to list but they are imutable - meaning you can't modify them.
example_tuple = ('Math','History')
# sets are valus that are unordered and no duplicates
example_set = {'Math','History'}
# sets throw away duplicates. Sets can also determine what values are shared with other sets