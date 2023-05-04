# Date time formats are extremely important to learn and you will use them in a lot of python applications. 

import datetime

# d = datetime.date(2016, 7, 24) # Single digits (no prefixed 0s) this works only with year, month, and day

# print(d)

# today = datetime.date.today() # get current date

# # print(today) # full date
# # print(today.year)  # year
# # print(today.month) #month
# # print(today.day) # day

# # print(today.weekday()) # numeric day value where monday is 1 and Sunday is 6
# # print(today.isoweekday()) # numeric day value where monday is 0 and Sunday is 7

# # let's take a look at time deltas. Time deltas are usefeul when we are looking at the difference between two dates. 

# tedelta = datetime.timedelta(days=7) 
# # we want to print out what the date will be one week from now. 

# print(today + tedelta) #what's the date 1 week from now
# print(today - tedelta) #what's the date 1 week ago from now

# # Above we were adding and subtracting a time delta from a date and getting another date as the result. Ex: date2 = date1 + timedelta
# # If we instead add or subract a date from a date for my date then we'll get a time delta as the result. Ex: timedelta = date1 + date2

# # example problem. let's figure out how many days there are until my bday this year. To calculate that we'll have to subtract the current date from the date of my bday.

# bday = datetime.date(2023, 10, 14)

# till_bday = bday - today
# print(till_bday)

# now let's look at datetime.time

t = datetime.time(9, 30, 45, 100000) # here we work with hours, min, seconds, andmicroseconds. does not include year,  month, day.

print(t)
print(t.hour) # access diff time elements

# then there is datetime.datetime which will give us access to everything. 

dt = datetime.datetime(2016,7,26,12,30,45,100000)
print(dt)
print(dt.date()) # grab date
print(dt.time()) # grab time
print(dt.year) # grab individual element like before. 